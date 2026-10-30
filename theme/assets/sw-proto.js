/* Swansura front end: the prototype's behaviours (prototype/index.html) on Shopify data.
   Overlays (drawer, search, bag) render into #layer with the prototype's markup; the bag uses the AJAX cart,
   search uses the Section Rendering API (section sw-p-search-results), the wishlist lives in localStorage. */
(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const cfg = JSON.parse($('#sw-config')?.textContent || '{}');
  const money = c => '£' + (c / 100).toFixed(2);
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const layer = () => $('#layer');
  const store = { get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch (e) { return d; } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} } };
  const offers = cfg.offers || { delivery: 40, bonus: { min: 70, off: 5 } };
  /* UK delivery rates in Shopify (user, 27 Oct 2026): standard £1.99 under the free-delivery threshold, two-day £2.99, next-day £3.99 */
  const ship = cfg.ship || { std: 1.99, two: 2.99, next: 3.99 };
  const shipOpts = total => `<div class="shipopts" role="group" aria-label="UK delivery options"><div class="so-h">UK delivery <small>Choose at checkout</small></div>
      <div class="so"><span>Standard <small>3–4 business days</small></span><b>${total >= offers.delivery ? 'Free' : '£' + ship.std.toFixed(2)}</b></div>
      <div class="so"><span>Two-day <small>2 business days</small></span><b>£${ship.two.toFixed(2)}</b></div>
      <div class="so"><span>Next-day <small>Next business day</small></span><b>£${ship.next.toFixed(2)}</b></div></div>`;
  const nextGoal = t => t < offers.delivery ? { goal: offers.delivery, left: offers.delivery - t, what: 'free UK delivery' }
    : t < offers.bonus.min ? { goal: offers.bonus.min, left: offers.bonus.min - t, what: `£${offers.bonus.off} off your order` } : null;
  const icon = {
    truck: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17" r="1.8"/><circle cx="17" cy="17" r="1.8"/></svg>',
    ret: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 10h11a5 5 0 0 1 0 10H8"/><path d="m8 6-4 4 4 4"/></svg>',
    lock: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="5" y="10" width="14" height="10"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>'
  };

  /* ---------- toast ---------- */
  function toast(msg) {
    const t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); t.textContent = msg;
    (document.querySelector('.swp-fixed') || document.body).appendChild(t); setTimeout(() => t.remove(), 2600);
  }
  window.swToast = toast;

  /* ---------- layer ---------- */
  function openLayer(html) { layer().innerHTML = html; document.documentElement.style.overflow = 'hidden'; }
  function closeLayer() { layer().innerHTML = ''; document.documentElement.style.overflow = ''; }

  /* ---------- bag ---------- */
  let cart = null;
  async function getCart() { cart = await (await fetch('/cart.js', { headers: { Accept: 'application/json' } })).json(); setCount(); return cart; }
  function setCount() {
    const c = $('#bagCount'), n = cart ? cart.item_count : 0; if (!c) return;
    c.hidden = n < 1; c.textContent = n > 99 ? '99+' : n;
    const b = $('#openBag'); if (b) b.setAttribute('aria-label', n ? `Open bag, ${n} item${n === 1 ? '' : 's'}` : 'Open bag');
  }
  async function addItems(items) {
    const r = await fetch('/cart/add.js', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ items }) });
    if (!r.ok) { const e = await r.json().catch(() => ({})); toast(e.description || 'Sorry, that could not be added'); return false; }
    return true;
  }
  async function change(key, quantity) {
    await fetch('/cart/change.js', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ id: key, quantity }) });
  }
  const pic = (src, alt) => src ? `<img class="pic" src="${esc(src)}${src.includes('?') ? '&' : '?'}width=200" alt="${esc(alt)}" width="200" height="250">` : '<div class="pic"></div>';
  async function openBag(justAdded) {
    await getCart();
    const total = cart.total_price / 100, ng = nextGoal(total);
    const inBag = new Set(cart.items.map(i => i.variant_id));
    const extras = (cfg.extras || []).filter(x => !inBag.has(x.id)).sort((a, b) => a.price - b.price).slice(0, 6);
    const lines = cart.items.length ? cart.items.map(l => `<div class="line${l.variant_id == justAdded ? ' just' : ''}">${pic(l.image, l.product_title)}<div><div style="font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--brass-ink)">${esc(l.vendor)}</div><a href="${esc(l.url)}" data-close>${esc(l.product_title)}${l.variant_title && !/default/i.test(l.variant_title) ? ' · ' + esc(l.variant_title) : ''}</a><div class="bq"><div class="qty sm"><button data-bq="${esc(l.key)}|${l.quantity - 1}" aria-label="Decrease quantity">−</button><span>${l.quantity}</span><button data-bq="${esc(l.key)}|${l.quantity + 1}" aria-label="Increase quantity">+</button></div><button class="rm" data-bq="${esc(l.key)}|0">Remove</button></div></div><div>${money(l.final_line_price)}</div></div>`).join('')
      : `<div class="bag-empty"><p>Your bag is empty.</p><a class="btn solid" href="/collections/all" data-close>Shop bestsellers</a><a class="p-link" href="/pages/rituals" data-close>Or start with a routine</a></div>`;
    const discount = cart.total_discount > 0 ? `<div style="display:flex;justify-content:space-between;font-size:14px;color:var(--emerald)"><span>Savings</span><b>−${money(cart.total_discount)}</b></div>` : '';
    const page = $('#bagPage');
    (page ? h => { page.innerHTML = h.replace(/^<div class="scrim" data-close><\/div>\s*/, '').replace('role="dialog" aria-modal="true"', 'role="region"'); } : openLayer)(`<div class="scrim" data-close></div>
  <div class="bag" role="dialog" aria-modal="true" aria-label="Your bag">
    <div class="bag-head"><h3>Your bag</h3><button data-close aria-label="Close bag">Close</button></div>
    <div class="bag-body">
    <div class="lines">${lines}</div>
    ${cart.items.length ? `<div class="delivery" style="border:0;padding:0;background:none"><span>${ng ? `You're <b>£${ng.left.toFixed(2)}</b> away from ${ng.what}${total >= offers.delivery ? ' (free UK delivery unlocked)' : ''}` : `<b>Free UK delivery + £${offers.bonus.off} off unlocked</b> (applied at checkout)`}</span><div class="bar"><i style="width:${Math.min(100, total / (ng ? ng.goal : 1) * 100)}%"></i></div></div>${shipOpts(total)}` : ''}
    ${extras.length && cart.items.length ? `<div class="bag-extras"><div class="eyebrow" style="margin-bottom:8px">Little extras</div><div class="extras">${extras.map(x => `<div class="extra">${pic(x.img, x.title)}<span>${esc(x.title)}</span><b>${money(x.price)}</b><button data-add="${x.id}">Add</button></div>`).join('')}</div></div>` : ''}
    <div class="bag-trust"><span>${icon.truck} Dispatched in 1–2 days</span><span>${icon.ret} <a href="${esc(cfg.returnsUrl || '/policies/refund-policy')}" data-close>Returns policy</a></span><span>${icon.lock} Secure checkout</span></div>
    <span class="pays" aria-label="Payment methods">${$('#swPayIcons')?.innerHTML || (cfg.pays || []).map(x => `<span class="pay">${esc(x)}</span>`).join('')}</span>
    </div>
    <div class="foot">
      ${discount}${cart.items.length ? `<div class="bag-ship"><span>Standard delivery</span><b>${total >= offers.delivery ? 'Free' : '£' + ship.std.toFixed(2)}</b></div>` : ''}<div class="bag-sub"><span>Subtotal${cart.item_count ? ` (${cart.item_count} item${cart.item_count === 1 ? '' : 's'})` : ''}</span><b>${money(cart.total_price)}</b></div>
      <p class="bag-note">Taxes included. Delivery and discount codes are added at checkout.</p>
      <a class="btn solid" id="checkoutBtn" href="/checkout"${cart.items.length ? '' : ' aria-disabled="true" style="pointer-events:none;opacity:.5"'}>Checkout securely</a>
      ${page ? '' : `<a class="p-link bag-view" href="/cart">View bag</a>`}
    </div>
  </div>`);
  }
  /* After 'Add': phones get a small bar at the bottom (user, 27 Oct 2026: the full-screen drawer got in the way);
     desktop and the bag page keep the drawer / inline bag. */
  const phone = () => matchMedia('(max-width: 720px)').matches;
  let addedTimer;
  async function added(justAdded, msg) {
    if (!phone() || $('#bagPage')) { if (msg) toast(msg); return openBag(justAdded); }
    await getCart();
    const l = cart.items.find(i => String(i.variant_id) === String(justAdded)) || cart.items[0];
    const total = cart.total_price / 100, ng = nextGoal(total);
    $('#addedBar')?.remove(); clearTimeout(addedTimer);
    const bar = document.createElement('div'); bar.id = 'addedBar'; bar.className = 'addedbar'; bar.setAttribute('role', 'status');
    bar.innerHTML = `${l ? pic(l.image, l.product_title) : ''}<div class="ab-txt"><b>${esc(msg || 'Added to your bag')}</b>${l ? `<span>${esc(l.product_title)}</span>` : ''}<small>${ng ? `£${ng.left.toFixed(2)} away from ${ng.what}` : `Free UK delivery + £${offers.bonus.off} off unlocked`}</small></div><a class="btn solid" href="/cart">View bag (${cart.item_count})</a><button class="ab-x" type="button" aria-label="Close">×</button>`;
    (document.querySelector('.swp-fixed') || document.body).appendChild(bar);
    bar.querySelector('.ab-x').addEventListener('click', () => bar.remove());
    addedTimer = setTimeout(() => bar.remove(), 6000);
  }
  /* Sold out: 'Notify' opens a small email pop-up (user, 27 Oct 2026) instead of sending shoppers to the product
     page and then the contact page. The request goes to the store inbox through Shopify's contact form. */
  function backInStock(title, url) {
    openLayer(`<div class="scrim" data-close></div><form class="bis" role="dialog" aria-modal="true" aria-labelledby="bisT" novalidate>
      <button type="button" class="bis-x" data-close aria-label="Close">×</button>
      <span class="eyebrow">Back in stock</span><h3 id="bisT">Get an email when it's back</h3><p class="bis-p">${esc(title)}</p>
      <label class="sr-only" for="bisE">Email address</label><input id="bisE" type="email" name="email" placeholder="Your email address" autocomplete="email" required>
      <button class="btn solid" type="submit">Notify me</button><p class="bis-note">We'll only use your email to tell you when this product is back.</p></form>`);
    const f = $('.bis'), inp = $('#bisE'); setTimeout(() => inp.focus(), 50);
    f.addEventListener('submit', async ev => {
      ev.preventDefault(); const email = inp.value.trim();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { inp.setAttribute('aria-invalid', 'true'); inp.focus(); return; }
      const fd = new FormData(); fd.append('form_type', 'contact'); fd.append('utf8', '✓'); fd.append('contact[email]', email);
      fd.append('contact[Request]', 'Back in stock'); fd.append('contact[Product]', title); fd.append('contact[body]', `Back-in-stock request: ${title} – ${location.origin}${url || ''}`);
      const btn = f.querySelector('[type=submit]'); btn.disabled = true; btn.textContent = 'Sending…';
      try {
        const r = await fetch('/contact#contact_form', { method: 'POST', body: fd });
        if (/challenge/.test(r.url)) { // Shopify's spam check: send the same request as a normal form so the shopper can confirm
          const real = document.createElement('form'); real.method = 'post'; real.action = '/contact#contact_form'; real.hidden = true;
          for (const [k, v] of fd) { const i = document.createElement('input'); i.name = k; i.value = v; real.appendChild(i); }
          document.body.appendChild(real); real.submit(); return; }
        f.innerHTML = `<button type="button" class="bis-x" data-close aria-label="Close">×</button><span class="eyebrow">Back in stock</span><h3>Thank you</h3><p class="bis-p">We'll email <b>${esc(email)}</b> when ${esc(title)} is back.</p><button type="button" class="btn solid" data-close>Continue shopping</button>`;
      } catch (err) { btn.disabled = false; btn.textContent = 'Notify me'; toast('Sorry, that did not send. Please try again.'); }
    });
  }
  function burst(t) {
    if (reduce) return; const r = t.getBoundingClientRect();
    for (let i = 0; i < 9; i++) { const b = document.createElement('i'); b.className = 'burst'; const a = Math.PI * 2 * i / 9 + Math.random() * .4, d = 22 + Math.random() * 22;
      b.style.left = (r.left + r.width / 2) + 'px'; b.style.top = (r.top + r.height / 2) + 'px'; b.style.setProperty('--dx', Math.cos(a) * d + 'px'); b.style.setProperty('--dy', Math.sin(a) * d + 'px'); b.style.setProperty('--s', (5 + Math.random() * 7) + 'px');
      (document.querySelector('.swp-fixed') || document.body).appendChild(b); setTimeout(() => b.remove(), 720); }
  }
  window.swOpenBag = openBag; window.swAddItems = addItems;

  /* ---------- search ---------- */
  let qTimer;
  function openSearch() {
    openLayer(`<div class="scrim" data-close></div><div class="search" role="dialog" aria-label="Search"><div class="wrap" style="padding:0;display:flex;flex-direction:column;gap:20px"><div style="display:flex;justify-content:space-between;align-items:center"><span class="eyebrow">Search ${esc(cfg.count || '')} products</span><button data-close>Close</button></div><form action="/search" method="get" role="search" style="margin:0"><input type="hidden" name="type" value="product"><label for="q" class="sr-only">Search products and brands</label><input id="q" name="q" placeholder="Search Deyga, oud, serum, Gucci…" autocomplete="off"></form><div id="qres"></div></div></div>`);
    const q = $('#q'); q.focus();
    const chips = () => `<div class="chips">${['Deyga', 'Vilvah', 'Oud', 'Lip balm', 'Serum', 'Al Haramain', 'Gucci', 'Gift set'].map(s => `<button class="chip" data-suggest="${s}">${s}</button>`).join('')}</div>`;
    const run = () => { clearTimeout(qTimer); const v = q.value.trim(); if (v.length < 2) { $('#qres').innerHTML = chips(); return; }
      qTimer = setTimeout(async () => { const html = await (await fetch(`/search?q=${encodeURIComponent(v)}&type=product&options[prefix]=last&section_id=sw-p-search-results`)).text();
        const d = new DOMParser().parseFromString(html, 'text/html'), r = d.querySelector('#sw-qres'); if (q.value.trim() === v && r) $('#qres').innerHTML = r.innerHTML; syncHearts(); }, 180); };
    q.addEventListener('input', run); run();
  }

  /* ---------- wishlist ---------- */
  let wish = store.get('swansura-wish', []);
  function syncHearts() {
    $$('[data-wish]').forEach(b => { const on = wish.includes(b.dataset.wish); b.setAttribute('aria-pressed', on); b.setAttribute('aria-label', (on ? 'Remove from' : 'Save to') + ' wishlist'); });
    const c = $('#wishCount'); if (c) { c.hidden = !wish.length; c.textContent = wish.length > 99 ? '99+' : wish.length; }
  }
  window.swWish = () => wish;

  /* ---------- clicks ---------- */
  document.addEventListener('click', async e => {
    const wb = e.target.closest('[data-wish]');
    if (wb) { e.preventDefault(); const id = wb.dataset.wish, on = !wish.includes(id); wish = on ? [id, ...wish] : wish.filter(x => x !== id); store.set('swansura-wish', wish); syncHearts(); toast(on ? 'Saved to your wishlist' : 'Removed from your wishlist'); document.dispatchEvent(new CustomEvent('sw:wish')); return; }
    const sg = e.target.closest('[data-suggest]'); if (sg) { const q = $('#q'); q.value = sg.dataset.suggest; q.dispatchEvent(new Event('input')); return; }
    const bis = e.target.closest('[data-backinstock]'); if (bis) { e.preventDefault(); backInStock(bis.dataset.backinstock, bis.dataset.url); return; }
    const nt = e.target.closest('[data-notify]'); if (nt) { toast('Thanks. We will email you when the ' + (nt.dataset.notify === 'skin' ? 'Skin' : 'Scent') + ' Studio Advent launches'); return; }
    const t = e.target.closest('[data-add],[data-addall],[data-bq],[data-close],[data-tab],#openBag,#openSearch,#burger,#drawerSearch');
    if (!t) { if (e.target.closest('.drawer-nav a')) closeLayer(); return; }
    if (t.dataset.add) { e.preventDefault(); if (t.classList.contains('add')) burst(t); t.disabled = true;
      if (await addItems([{ id: +t.dataset.add, quantity: 1 }])) await added(t.dataset.add); t.disabled = false; return; }
    if (t.dataset.addall) { e.preventDefault(); if (await addItems(t.dataset.addall.split(',').map(id => ({ id: +id, quantity: 1 })))) { await added(t.dataset.addall.split(',')[0], 'Ritual added to your bag'); } return; }
    if (t.dataset.bq) { const [key, q] = t.dataset.bq.split('|'); await change(key, Math.max(0, +q)); await openBag(); return; }
    if ('close' in t.dataset) { if (t.tagName !== 'A') e.preventDefault(); closeLayer(); return; }
    if (t.dataset.tab) { $$('.tabs [data-tab]').forEach(b => b.setAttribute('aria-selected', b === t)); const g = $('#bestGrid'), src = $('#best-' + t.dataset.tab); if (g && src) { g.innerHTML = src.innerHTML; syncHearts(); } return; }
    if (t.id === 'openBag') return; // the bag icon opens the bag page (/cart); the drawer only opens after adding
    if (t.id === 'openSearch') { e.preventDefault(); openSearch(); return; }
    if (t.id === 'burger') { const tp = $('#sw-drawer-tpl'); if (tp) openLayer(tp.innerHTML); return; }
    if (t.id === 'drawerSearch') { closeLayer(); openSearch(); }
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && layer()?.innerHTML) closeLayer(); });

  // Motion (hero slider, announcement rotation) starts on the shopper's first scroll / tap / mouse move / key, or 8 s
  // after load, so the page settles before anything moves (PageSpeed: Speed Index + LCP, 27–28 Oct 2026)
  const afterLoad = (() => { const q = []; let started = false;
    const start = () => { if (started) return; started = true; EV.forEach(t => removeEventListener(t, start, opts)); q.splice(0).forEach(f => f()); };
    const EV = ['pointerdown', 'pointermove', 'touchstart', 'scroll', 'keydown', 'wheel'], opts = { passive: true };
    EV.forEach(t => addEventListener(t, start, opts));
    const later = () => setTimeout(start, 8000); if (document.readyState === 'complete') later(); else addEventListener('load', later, { once: true });
    return fn => { if (started) fn(); else q.push(fn); }; })();

  /* ---------- footer wordmark shimmer only while the footer is on screen (PageSpeed, 28 Oct 2026) ---------- */
  (() => { const w = $('footer .fmark-wrap'); if (!w || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(es => es.forEach(e => w.classList.toggle('inview', e.isIntersecting))).observe(w); })();

  /* ---------- announcement bar: one message at a time where they don't fit side by side ---------- */
  (() => { const items = $$('.announce .wrap>*'); if (items.length < 2) return; let i = 0; items[0].classList.add('on');
    // always one line (user, 27 Oct 2026): side by side when all messages fit, otherwise one at a time
    const bar = $('.announce'), wrap = $('.announce .wrap');
    const fit = () => { bar.classList.remove('rot'); if (wrap.scrollWidth > wrap.clientWidth + 1) bar.classList.add('rot'); };
    fit(); addEventListener('resize', fit); document.fonts?.ready.then(fit);
    afterLoad(() => setInterval(() => { items[i].classList.remove('on'); i = (i + 1) % items.length; items[i].classList.add('on'); }, 1000)); })();

  /* ---------- hero: skin + scent pairs slide together ---------- */
  (() => { const st = $('.hero .stage'); if (!st) return; const tracks = $$('.track', st), n = tracks[0]?.children.length || 0; let i = 0, timer;
    const go = k => { i = (k + n) % n; tracks.forEach(t => { t.style.transform = `translateX(-${i * 100}%)`; [...t.children].forEach((a, j) => { a.tabIndex = j === i ? 0 : -1; a.setAttribute('aria-hidden', j !== i); }); }); };
    const play = () => { clearInterval(timer); if (!reduce && n > 1) timer = setInterval(() => go(i + 1), 1000); };
    st.onmouseenter = st.onfocusin = () => clearInterval(timer); st.onmouseleave = st.onfocusout = play;
    let x0 = null; st.ontouchstart = e => { x0 = e.touches[0].clientX; clearInterval(timer); };
    st.ontouchend = e => { if (x0 != null) { const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) go(i + (dx < 0 ? 1 : -1)); x0 = null; } play(); };
    go(0); afterLoad(play); })();

  /* ---------- popular searches: on desktop the cards are dropdowns, one open at a time ---------- */
  (() => { const g = $('#popular .searches'); if (!g) return; const all = () => [...g.querySelectorAll('details')];
    g.addEventListener('toggle', e => { if (!phone() && e.target.open) all().forEach(d => { if (d !== e.target) d.open = false; }); }, true);
    document.addEventListener('click', e => { if (!phone() && !e.target.closest('#popular .searches')) all().forEach(d => { d.open = false; }); });
    document.addEventListener('keydown', e => { if (e.key !== 'Escape') return; const o = all().find(d => d.open); if (o && !phone()) { o.open = false; o.querySelector('summary').focus(); } }); })();

  /* ---------- shopping assistant (help panel; user, 30 Oct 2026) ----------
     A guided chat: the shopper picks a need (concern, hair, body, perfume, gift, brand, orders), answers 1–3 short
     questions and gets real products from the matching collection (/collections/<handle>?view=assist, section
     sw-p-assist) filtered by skin type, scent family and budget. Typed text is matched to a known need or brand,
     else Shopify's predictive search. No AI and no invented answers: order questions get the store's own facts
     and a person on WhatsApp / Instagram / email. Every chip carries the whole state, so the log can be restored. */
  (() => {
    const b = $('#chatBtn'), p = $('#chatPanel'); if (!b || !p) return;
    const log = $('#asLog', p), form = $('#asForm', p), q = $('#asQ', p), bar = $('.as-bar i', p), resetBtn = $('[data-asreset]', p);
    const KEY = 'swAssist', ss = { get() { try { return JSON.parse(sessionStorage.getItem(KEY)); } catch (e) { return null; } }, set(v) { try { sessionStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {} } };
    const wa = p.dataset.wa, waLabel = p.dataset.waLabel, mail = p.dataset.email, ig = p.dataset.ig;
    const BUDGET = [['0-1500', 'Under £15'], ['1500-3000', '£15 to £30'], ['3000-5000', '£30 to £50'], ['5000-', 'Over £50'], ['', 'Any budget']];
    const BRANDS = [["Abercrombie & Fitch", "abercrombie-fitch"], ["Acqua di Parma", "acqua-di-parma"], ["Al Haramain", "al-haramain"], ["anatomē", "anatome"], ["Anna Sui", "anna-sui"], ["Antonio Banderas", "antonio-banderas"], ["Ariana Grande", "ariana-grande"], ["Armaf", "armaf"], ["Azzaro", "azzaro"], ["Bentley", "bentley"], ["Boucheron", "boucheron"], ["Burberry", "burberry"], ["Bvlgari", "bvlgari"], ["Calvin Klein", "calvin-klein"], ["Carolina Herrera", "carolina-herrera"], ["Chloé", "chloe"], ["Chopard", "chopard"], ["Coach", "coach"], ["Davidoff", "davidoff"], ["Deyga", "deyga"], ["Dior", "dior"], ["DKNY", "dkny"], ["Dolce & Gabbana", "dolce-gabbana"], ["Dunhill", "dunhill"], ["Elie Saab", "elie-saab"], ["Elizabeth Arden", "elizabeth-arden"], ["Escada", "escada"], ["Estée Lauder", "estee-lauder"], ["Etienne Aigner", "etienne-aigner"], ["Fumeri", "fumeri"], ["Giorgio Armani", "giorgio-armani"], ["Givenchy", "givenchy"], ["Gucci", "gucci"], ["Guerlain", "guerlain"], ["Hemel", "hemel"], ["Hermès", "hermes"], ["Highborn London", "highborn-london"], ["Hollister", "hollister"], ["Hugo Boss", "hugo-boss"], ["Jean Paul Gaultier", "jean-paul-gaultier"], ["Jimmy Choo", "jimmy-choo"], ["Jo Milano", "jo-milano"], ["John Varvatos", "john-varvatos"], ["Joop!", "joop"], ["Juicy Couture", "juicy-couture"], ["Kenneth Cole", "kenneth-cole"], ["Korloff", "korloff"], ["La Maison", "la-maison"], ["Lancôme", "lancome"], ["Mancera", "mancera"], ["Marc Jacobs", "marc-jacobs"], ["Montale", "montale"], ["Nina Ricci", "nina-ricci"], ["Paloma Picasso", "paloma"], ["Philipp Plein", "philipp-plein"], ["S.T. Dupont", "s-t-dupont"], ["SAP", "sap"], ["Serge Lutens", "serge-lutens"], ["Shiseido", "shiseido"], ["Signature D'orient", "signature-dorient"], ["Swansura Selection", "swansura-selection"], ["The Woods Collection", "the-woods-collection"], ["Tiziana Terenzi", "tiziana-terenzi"], ["Tom Ford", "tom-ford"], ["Trussardi", "trussardi"], ["Viktor & Rolf", "viktor-rolf"], ["Vilvah", "vilvah"], ["Yves Saint Laurent", "yves-saint-laurent"]];
    const TOP_BRANDS = ['Deyga', 'Vilvah', 'Highborn London', 'anatomē', 'Al Haramain', 'Tiziana Terenzi', 'Jo Milano', 'Tom Ford', 'Dior', 'Gucci', 'Giorgio Armani', 'Montale'];
    const START = [['skin', 'Skincare for a concern'], ['hair', 'Haircare'], ['body', 'Body care'], ['perfume', 'Find a perfume'], ['gift', 'A gift'], ['brand', 'Shop by brand'], ['help', 'Delivery, returns & orders']];
    /* each flow: steps (key, question, options [value, label]) then the collection to show: src(state) */
    const FLOWS = {
      skin: { name: 'skincare', steps: [
        { k: 'h', q: 'What would you most like help with?', o: [['concern-hydration', 'Dryness & hydration'], ['concern-glow', 'Dullness & glow'], ['concern-acne', 'Spots & oily skin'], ['concern-calm', 'Sensitive skin'], ['concern-lips', 'Dry lips'], ['concern-sun', 'Sun protection']] },
        { k: 's', q: 'And how would you describe your skin?', o: [['Dry', 'Dry'], ['Oily', 'Oily'], ['Combination', 'Combination'], ['Sensitive', 'Sensitive'], ['', 'Not sure']], skip: st => st.h === 'concern-lips' || st.h === 'concern-sun' },
        { k: 'b', q: 'Last one: what budget per product?', o: BUDGET }] },
      hair: { name: 'haircare', steps: [
        { k: 'h', q: 'What is your hair asking for?', o: [['concern-hairfall', 'Hair fall'], ['concern-dandruff', 'Dandruff & flakes'], ['hair-oil-for-dry-hair', 'Dry or frizzy hair'], ['hair-oil', 'A nourishing hair oil'], ['natural-shampoo', 'A gentle shampoo']] },
        { k: 'b', q: 'What budget per product?', o: BUDGET }] },
      body: { name: 'body care', steps: [
        { k: 'h', q: 'What are you looking for?', o: [['body-butter-for-dry-skin', 'Rich care for dry skin'], ['body-scrub', 'A body scrub'], ['shower-gel-body-wash', 'Shower & bath'], ['deodrants', 'Natural deodorant'], ['lip-balm', 'Lip balm']] },
        { k: 'b', q: 'What budget per product?', o: BUDGET }] },
      perfume: { name: 'perfume', steps: [
        { k: 'h', q: 'Lovely. Who is the perfume for?', o: [['perfume-for-women', 'For her'], ['perfume-for-men', 'For him'], ['unisex-perfume', 'Anyone (unisex)'], ['fragrance', 'Not sure yet']] },
        { k: 'f', q: 'Which scent mood do you love?', o: [['floral', 'Floral & soft'], ['woody', 'Woody & warm'], ['oud', 'Rich oud'], ['amber', 'Amber & sweet'], ['fresh', 'Fresh & clean'], ['', 'Surprise me']] },
        { k: 'b', q: 'And your budget?', o: BUDGET }] },
      gift: { name: 'gifts', steps: [
        { k: 'h', q: 'How exciting. Who are you shopping for?', o: [['gifts-for-her', 'Her'], ['gifts-for-him', 'Him'], ['perfume-gift-sets', 'Perfume gift sets'], ['giftsets', 'Skincare gift sets'], ['stocking-fillers', 'Stocking fillers']] },
        { k: 'b', q: 'What would you like to spend?', o: BUDGET }] },
      brand: { name: 'brand', steps: [
        { k: 'h', q: 'Which brand would you like to see? You can also type any brand below.', o: [...TOP_BRANDS.map(n => [BRANDS.find(x => x[0] === n)[1], n]), ['@/collections', 'All brands A–Z']] }] }
    };
    const HELP = {
      delivery: ['Delivery', `UK delivery, dispatched from the UK within 1–2 working days:<ul><li><b>Standard</b> £${ship.std.toFixed(2)}, 3–4 business days, <b>free over £${offers.delivery}</b></li><li><b>Two-day</b> £${ship.two.toFixed(2)}</li><li><b>Next-day</b> £${ship.next.toFixed(2)}</li></ul>Spend £${offers.bonus.min} and you also get £${offers.bonus.off} off at checkout.`, [['/pages/shipping', 'Delivery details']]],
      returns: ['Returns', 'You can return unopened, sealed items within 14 days of delivery; return postage is paid by you. If something arrives faulty, damaged or wrong, we put it right at no cost.', [[cfg.returnsUrl || '/pages/shipping', 'Returns policy']]],
      track: ['Track my order', 'Your shipping confirmation email has a tracking link. You can also sign in to see your orders, or message us with your order number and we will check for you.', [['/account', 'My account']]],
      authentic: ['Is it authentic?', 'Yes. Everything we sell is 100% authentic, and we are the official UK partner of Deyga and Vilvah. Orders ship from the UK.', [['/pages/about', 'About Swansura']]],
      pay: ['Ways to pay', 'Cards (Visa, Mastercard, Amex, Maestro), PayPal, Apple Pay, Google Pay and Shop Pay. With PayPal you can split £30 to £2,000 into 3 interest-free payments.', []]
    };
    const brandName = h => (BRANDS.find(x => x[1] === h) || [])[0];
    const label = (fl, k, v) => { const s = FLOWS[fl]?.steps.find(x => x.k === k); return (s?.o.find(o => o[0] === v) || [])[1] || v; };
    const go = st => esc(JSON.stringify(st));
    const chips = (opts, extra = '') => `<div class="as-chips${extra}">${opts.map(([st, l]) => `<button type="button" class="as-chip" data-go="${go(st)}">${esc(l)}</button>`).join('')}</div>`;
    const save = () => ss.set({ html: log.innerHTML, bar: bar.style.width });
    const scroll = el => { const top = el.offsetTop - 8; log.scrollTo({ top, behavior: reduce ? 'auto' : 'smooth' }); };
    const lockOld = () => $$('.as-chips:not(.keep) .as-chip', log).forEach(c => { c.disabled = true; });
    function you(text) { lockOld(); log.insertAdjacentHTML('beforeend', `<div class="as-msg you"><p>${esc(text)}</p></div>`); }
    async function bot(html) {
      if (!reduce) { log.insertAdjacentHTML('beforeend', '<div class="as-msg bot as-typing" aria-hidden="true"><p><i></i><i></i><i></i></p></div>'); const t = log.lastElementChild; scroll(t); await new Promise(r => setTimeout(r, 420)); t.remove(); }
      log.insertAdjacentHTML('beforeend', `<div class="as-msg bot">${html}</div>`); const m = log.lastElementChild; scroll(m); resetBtn.hidden = false; save();
      const f = m.querySelector('.as-chip:not([disabled]), .as-card .as-ct a'); if (f && p.contains(document.activeElement) && !matchMedia('(pointer:coarse)').matches) f.focus({ preventScroll: true });
      return m;
    }
    const people = () => `<div class="as-people">${wa ? `<a class="as-person wa" href="https://wa.me/${esc(wa)}" target="_blank" rel="noopener"><b>WhatsApp</b><small>${esc(waLabel)} · messages only</small></a>` : ''}${ig ? `<a class="as-person ig" href="${esc(ig)}" target="_blank" rel="noopener"><b>Instagram</b><small>@swansura_thebodystudio</small></a>` : ''}${mail ? `<a class="as-person em" href="mailto:${esc(mail)}"><b>Email</b><small>${esc(mail)}</small></a>` : ''}</div>`;
    const greet = () => { const h = new Date().getHours(); return h < 12 ? 'Good morning' : h < 18 ? 'Good afternoon' : 'Good evening'; };
    async function start() {
      log.innerHTML = ''; bar.style.width = '0%'; resetBtn.hidden = true;
      await bot(`<p><b>${greet()}, welcome to Swansura.</b> I can help you find the right product in a few taps. What are you shopping for today?</p>${chips(START.map(([f, l]) => [{ f }, l]))}<p class="as-note">Prefer a person? <button type="button" class="as-link" data-go="${go({ f: 'help', a: 'person' })}">Message our team</button></p>`);
    }
    /* products of a collection (all pages), cached for the visit */
    const cache = {};
    // brand pages before the 30 Oct 2026 rename (tried when the new handle is not there yet)
    const LEGACY = { deyga: 'milk-drop-brightening-serum-1', vilvah: 'milk-drop-brightening-serum', 'jo-milano': 'luxury-collection-1', 'tom-ford': 'tomford', 'antonio-banderas': 'antonio', 'yves-saint-laurent': 'ysl', 'philipp-plein': 'phillip-plein', joop: 'joop-homme', 'jean-paul-gaultier': 'jean-paul', hemel: 'hemel-h', 'signature-dorient': 'signature-sillage-dorient' };
    async function products(h) {
      if (cache[h]) return cache[h];
      const all = []; let page = 1, pages = 1, count = 0, src = h;
      do { let r = await fetch(`/collections/${src}?view=assist&page=${page}`, { headers: { Accept: 'text/html' } });
        if (r.status === 404 && page === 1 && LEGACY[h]) { src = LEGACY[h]; r = await fetch(`/collections/${src}?view=assist&page=1`, { headers: { Accept: 'text/html' } }); }
        if (!r.ok) throw new Error(r.status);
        const t = await r.text(), m = t.match(/<script type="application\/json" id="swAssistData">([\s\S]*?)<\/script>/); if (!m) throw new Error('no data');
        const d = JSON.parse(m[1]); all.push(...d.products); pages = d.pages; count = d.count; page++; } while (page <= pages && page <= 4);
      return (cache[h] = { list: all, count });
    }
    const inBudget = (x, bgt) => { if (!bgt) return true; const [lo, hi] = bgt.split('-'); return x.p >= +lo && (hi === '' || x.p < +hi); };
    const card = x => `<div class="as-card"><a class="as-pic" href="${esc(x.u)}" tabindex="-1" aria-hidden="true">${x.i ? `<img src="${esc(x.i)}" alt="" width="64" height="80" loading="lazy">` : ''}</a><div class="as-ct"><small>${esc(x.b)}</small><a href="${esc(x.u)}">${esc(x.n)}</a><span class="as-pr">${money(x.p)}${x.c > x.p ? ` <s>${money(x.c)}</s>` : ''}</span></div>${x.a && x.v ? `<button type="button" class="as-add" data-add="${x.v}" aria-label="Add ${esc(x.n)} to bag">Add</button>` : x.a ? `<a class="as-add" href="${esc(x.u)}" aria-label="View ${esc(x.n)}">View</a>` : `<a class="as-add out" href="${esc(x.u)}">Sold out</a>`}</div>`;
    async function results(st) {
      const fl = FLOWS[st.f], h = st.h;
      let data; try { data = await products(h); } catch (e) { await bot(`<p>Sorry, I could not load those products just now.</p>${chips([[{ u: '/collections/' + h }, 'Open the collection'], [{ f: 'help', a: 'person' }, 'Ask our team']])}`); return; }
      const avail = data.list.filter(x => x.a);
      const tests = [['s', x => !st.s || !x.s.length || x.s.includes(st.s) || x.s.includes('All')], ['f', x => !st.f2 || x.f === st.f2], ['b', x => inBudget(x, st.b)]];
      let pick = avail.filter(x => tests.every(t => t[1](x))), relaxed = [];
      const active = { s: st.s, f: st.f2, b: st.b };
      for (const k of ['s', 'f', 'b']) { if (pick.length) break; if (!active[k]) continue; const keep = tests.filter(t => t[0] !== k && !relaxed.includes(t[0])); relaxed.push(k); pick = avail.filter(x => keep.every(t => t[1](x))); }
      if (!pick.length) pick = data.list;
      pick = [...pick.filter(x => x.k), ...pick.filter(x => !x.k)];
      const PERF = { 'perfume-for-women': 'perfume for her', 'perfume-for-men': 'perfume for him', 'unisex-perfume': 'unisex perfume', fragrance: 'perfume' };
      const what = st.f === 'brand' ? brandName(h) : PERF[h] ? [st.f2 && label('perfume', 'f', st.f2).toLowerCase(), PERF[h]].filter(Boolean).join(' ') : label(st.f, 'h', h).toLowerCase();
      const note = relaxed.length ? `<p class="as-note">Nothing matched every answer, so I widened the ${relaxed.map(k => ({ s: 'skin type', f: 'scent mood', b: 'budget' })[k]).join(' and ')}.</p>` : '';
      const first = pick.slice(0, 4), more = pick.slice(4, 12);
      bar.style.width = '100%';
      const next = [[{ u: '/collections/' + h }, `See all ${data.count}`]];
      if (fl && fl.steps.some(s => s.k === 'b') && st.b !== undefined) next.push([{ ...st, b: undefined, step: fl.steps.findIndex(s => s.k === 'b') }, 'Change budget']);
      next.push([{ f: st.f === 'brand' ? 'brand' : st.f }, st.f === 'brand' ? 'Another brand' : 'Try another answer'], [{ f: 'help', a: 'person' }, 'Ask a person']);
      await bot(`<p>${pick.length ? `Here ${first.length === 1 ? 'is my pick' : `are ${first.length} picks`} for <b>${esc(what)}</b>${st.b ? `, ${esc(label('perfume', 'b', st.b).toLowerCase())}` : ''}.` : 'Here is the collection.'}</p>${note}<div class="as-cards">${first.map(card).join('')}</div>${more.length ? `<div class="as-cards" hidden>${more.map(card).join('')}</div><button type="button" class="as-more" data-asmore>Show ${more.length} more</button>` : ''}${chips(next, ' keep')}`);
    }
    async function step(st) {
      const fl = FLOWS[st.f]; let i = st.step || 0;
      while (fl.steps[i] && (st[fl.steps[i].k === 'f' ? 'f2' : fl.steps[i].k] !== undefined || fl.steps[i].skip?.(st))) i++;
      const s = fl.steps[i];
      if (!s) return results(st);
      bar.style.width = Math.round(i / fl.steps.length * 100) + '%';
      const key = s.k === 'f' ? 'f2' : s.k;
      await bot(`<span class="as-step">Step ${i + 1} of ${fl.steps.length}</span><p>${esc(s.q)}</p>${chips(s.o.map(([v, l]) => v.startsWith('@') ? [{ u: v.slice(1) }, l] : [{ ...st, step: undefined, [key]: v }, l]))}`);
    }
    async function help(a) {
      bar.style.width = '0%';
      if (!a) return bot(`<p>Of course. What do you need help with?</p>${chips([...Object.entries(HELP).map(([k, v]) => [{ f: 'help', a: k }, v[0]]), [{ f: 'help', a: 'person' }, 'Talk to a person']])}`);
      if (a === 'person') return bot(`<p>Our team usually replies within a few hours, Monday to Friday. Pick whichever suits you:</p>${people()}${chips([[{}, 'Back to shopping']], ' keep')}`);
      const [, text, links] = HELP[a];
      return bot(`<div class="as-bub">${text}</div>${links.length ? `<p class="as-links">${links.map(([u, l]) => `<a href="${esc(u)}">${esc(l)} →</a>`).join('')}</p>` : ''}${chips([[{ f: 'help' }, 'Something else'], [{ f: 'help', a: 'person' }, 'Talk to a person'], [{}, 'Back to shopping']], ' keep')}`);
    }
    async function run(st) {
      if (st.u) { location.href = st.u; return; }
      if (!st.f) return start();
      if (st.f === 'help') return help(st.a);
      if (st.h && FLOWS[st.f]?.steps.length === 1) return results(st);
      return step(st);
    }
    /* typed text: order words → answers, a brand → its products, a need → its collection, else predictive search */
    const WORDS = [[/deliver|shipping|postage|dispatch/, { f: 'help', a: 'delivery' }], [/return|refund|exchange/, { f: 'help', a: 'returns' }], [/track|my order|where is/, { f: 'help', a: 'track' }], [/authentic|genuine|fake|original/, { f: 'help', a: 'authentic' }], [/\bpay|paypal|klarna|instal/, { f: 'help', a: 'pay' }], [/human|person|talk|contact|whatsapp|call|speak/, { f: 'help', a: 'person' }],
      [/dry skin|hydrat|moistur/, { f: 'skin', h: 'concern-hydration' }], [/glow|dull|bright|radian/, { f: 'skin', h: 'concern-glow' }], [/acne|spot|breakout|pimple|oily skin/, { f: 'skin', h: 'concern-acne' }], [/sensitive|redness|calm/, { f: 'skin', h: 'concern-calm' }], [/\blips?\b|lip balm|lip scrub/, { f: 'skin', h: 'concern-lips', s: '' }], [/\bsun|spf/, { f: 'skin', h: 'concern-sun', s: '' }],
      [/hair ?fall|hair loss|thinning/, { f: 'hair', h: 'concern-hairfall' }], [/dandruff|flak/, { f: 'hair', h: 'concern-dandruff' }], [/frizz|dry hair/, { f: 'hair', h: 'hair-oil-for-dry-hair' }], [/hair oil/, { f: 'hair', h: 'hair-oil' }], [/shampoo/, { f: 'hair', h: 'natural-shampoo' }],
      [/body butter/, { f: 'body', h: 'body-butter-for-dry-skin' }], [/scrub/, { f: 'body', h: 'body-scrub' }], [/shower|body wash|soap/, { f: 'body', h: 'shower-gel-body-wash' }], [/deodor/, { f: 'body', h: 'deodrants' }],
      [/\boud\b/, { f: 'perfume', h: 'fragrance', f2: 'oud' }], [/perfume for (her|women)|women'?s perfume/, { f: 'perfume', h: 'perfume-for-women' }], [/perfume for (him|men)|men'?s (perfume|cologne)|aftershave/, { f: 'perfume', h: 'perfume-for-men' }], [/stocking/, { f: 'gift', h: 'stocking-fillers' }], [/gift/, { f: 'gift' }], [/perfume|fragrance|scent/, { f: 'perfume' }]];
    const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    async function ask(text) {
      const t = norm(text).trim(), br = BRANDS.find(([n]) => t.includes(norm(n)) || (norm(n).length > 4 && norm(n).includes(t) && t.length > 3));
      // a brand on its own ('vilvah', 'tom ford products') shows the brand; a brand + product words goes to search
      if (br && !(t.includes(norm(br[0])) ? t.replace(norm(br[0]), '') : '').replace(/\b(products?|brand|range|perfumes?|skincare|shop|all|the)\b/g, '').trim()) return results({ f: 'brand', h: br[1] });
      const w = WORDS.find(([re]) => re.test(t)); if (w) return run({ ...w[1] });
      try { const r = await fetch(`/search/suggest.json?q=${encodeURIComponent(text)}&resources[type]=product&resources[limit]=6&resources[options][unavailable_products]=last`), d = await r.json();
        const list = (d.resources?.results?.products || []).map(x => { const v = (x.variants || []).find(y => y.available) || (x.variants || [])[0] || {}; const pr = s => Math.round(parseFloat(String(s ?? '0')) * (String(s ?? '').includes('.') ? 100 : 1));
          return { u: x.url, n: x.title, b: x.vendor === 'Swansura - The Body Studio' ? 'Swansura Selection' : x.vendor, p: pr(v.price ?? x.price), c: pr(v.compare_at_price ?? x.compare_at_price_max ?? 0), a: x.available !== false && v.available !== false, v: v.id, i: x.featured_image?.url || x.image || '' }; });
        if (list.length) return bot(`<p>Here is what I found for <b>${esc(text)}</b>:</p><div class="as-cards">${list.slice(0, 4).map(card).join('')}</div>${chips([[{ u: '/search?q=' + encodeURIComponent(text) }, 'See all results'], [{}, 'Guide me instead']], ' keep')}`);
      } catch (e) {}
      return bot(`<p>I could not find a match for <b>${esc(text)}</b>. Shall I guide you, or would you like to ask our team?</p>${chips([[{}, 'Guide me'], [{ f: 'help', a: 'person' }, 'Ask a person']], ' keep')}`);
    }
    function set(open) {
      p.hidden = !open; b.setAttribute('aria-expanded', open); document.documentElement.classList.toggle('as-open', open);
      if (!open) return;
      if (!log.children.length) { const s = ss.get(); if (s?.html) { log.innerHTML = s.html; bar.style.width = s.bar || '0%'; resetBtn.hidden = false; log.scrollTop = log.scrollHeight; } else start(); }
      p.focus({ preventScroll: true });
    }
    b.addEventListener('click', () => set(p.hidden));
    p.addEventListener('click', e => {
      const c = e.target.closest('[data-go]');
      if (c) { if (c.disabled) return; const st = JSON.parse(c.dataset.go); if (!st.u) you(c.textContent.replace(/ →$/, '')); run(st); return; }
      if (e.target.closest('[data-asmore]')) { const m = e.target.closest('[data-asmore]'); m.previousElementSibling.hidden = false; m.remove(); save(); return; }
      if (e.target.closest('[data-asreset]')) { p.focus(); start(); return; }
      if (e.target.closest('[data-chatclose]')) set(false);
    });
    p.addEventListener('click', e => { if (e.target.closest('.as-card a, .as-links a, .as-person')) save(); }, true);
    form.addEventListener('submit', e => { e.preventDefault(); const t = q.value.trim(); if (!t) return; q.value = ''; you(t); ask(t); });
    document.addEventListener('click', e => { if (!p.hidden && matchMedia('(max-width:600px)').matches && e.target.closest('.as-scrim')) set(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !p.hidden) { set(false); b.focus(); } });
  })();

  /* ---------- share (shareMenu() in the prototype): native sheet on touch devices, else a menu ---------- */
  let shareOwner = null;
  const closeShares = () => { $$('.sharemenu').forEach(m => m.remove()); $$('[data-share][aria-expanded="true"]').forEach(b => b.setAttribute('aria-expanded', 'false')); shareOwner = null; };
  function placeShare(mn, b) { const bt = b.getBoundingClientRect(), r = mn.getBoundingClientRect(), gap = 8;
    let left = b.closest('.share.dark') ? bt.left : bt.right - r.width; left = Math.max(12, Math.min(left, innerWidth - r.width - 12));
    let top = bt.bottom + gap; if (top + r.height > innerHeight - 8 && bt.top - r.height - gap > 8) top = bt.top - r.height - gap;
    mn.style.left = left + 'px'; mn.style.top = top + 'px'; }
  const reShare = () => { const m = $('.sharemenu'); if (shareOwner && m) { if (!document.contains(shareOwner)) closeShares(); else placeShare(m, shareOwner); } };
  addEventListener('scroll', reShare, { passive: true }); addEventListener('resize', reShare);
  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-share]');
    if (b) { const url = new URL(b.dataset.share || location.pathname, location.origin).href, d = { url, title: b.dataset.shareTitle || document.title, text: b.dataset.shareText || document.title, img: b.dataset.shareImg || '' };
      if (navigator.share && matchMedia('(pointer:coarse)').matches) { try { await navigator.share({ title: d.title, text: d.text, url: d.url }); return; } catch (err) { if (err && err.name === 'AbortError') return; } }
      const open = shareOwner !== b; closeShares();
      if (open) { const u = encodeURIComponent(d.url), t = encodeURIComponent(d.text);
        const opts = [['WhatsApp', `https://wa.me/?text=${t}%20${u}`], ['Facebook', `https://www.facebook.com/sharer/sharer.php?u=${u}`], ['Pinterest', `https://pinterest.com/pin/create/button/?url=${u}&media=${encodeURIComponent(d.img)}&description=${t}`], ['X', `https://x.com/intent/post?text=${t}&url=${u}`], ['Email', `mailto:?subject=${encodeURIComponent(d.title)}&body=${t}%0A${u}`]];
        ($('.swp-fixed') || document.body).insertAdjacentHTML('beforeend', `<div class="sharemenu" role="menu" aria-label="Share this page">${opts.map(([n, h]) => `<a role="menuitem" href="${h}" target="_blank" rel="noopener">${n}</a>`).join('')}<button role="menuitem" data-sharecopy="${esc(d.url)}">Copy link</button><p class="sharelink">${esc(d.url)}</p></div>`);
        const mn = $('.sharemenu'); placeShare(mn, b); shareOwner = b; mn.querySelector('[role=menuitem]').focus({ preventScroll: true }); }
      b.setAttribute('aria-expanded', open); return; }
    const c = e.target.closest('[data-sharecopy]');
    if (c) { try { await navigator.clipboard.writeText(c.dataset.sharecopy); c.textContent = 'Link copied'; } catch (err) { const r = document.createRange(), l = c.parentElement.querySelector('.sharelink'); r.selectNodeContents(l); getSelection().removeAllRanges(); getSelection().addRange(r); c.textContent = 'Press Ctrl+C to copy'; } return; }
    if (!e.target.closest('.share,.sharemenu')) closeShares();
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && shareOwner) { const b = shareOwner; closeShares(); b.focus(); } });

  /* ---------- listing filters, sort and paging (listing() / applyFilters() in the prototype) ---------- */
  (() => {
    const root = $('[data-listing]'); if (!root) return;
    const pool = $('#sw-pool'), PAGE = 24, brandMode = 'brand' in root.dataset;
    const CONCERNS = { acne: 'Acne & oil control', glow: 'Glow & even tone', hydration: 'Deep hydration', lips: 'Lip care', sun: 'Sun care', hairfall: 'Hair fall', dandruff: 'Dandruff', calm: 'Calm & sleep' };
    const FAM = { oud: 'Oud', amber: 'Amber', floral: 'Floral', woody: 'Woody', fresh: 'Fresh' };
    let brandCount = {}; try { brandCount = JSON.parse($('#sw-brand-counts').textContent); } catch (e) {}
    const split = v => v ? v.split('|').filter(Boolean) : [];
    let all = [], shown = PAGE;
    const collect = () => { all = $$('article.p-card', pool).map((el, i) => ({ el, i, t: el.dataset.t || 'More', b: el.dataset.b, c: split(el.dataset.c), s: split(el.dataset.s), g: split(el.dataset.g), f: el.dataset.f, w: el.dataset.w, p: +el.dataset.p, ok: el.dataset.in === '1', n: el.dataset.n || '', r: +el.dataset.r || 9999 })); };
    function build() {
      const list = all, N = list.length;
      const cnt = (fn, v) => list.filter(p => fn(p).includes(v)).length;
      const mk = (h, f, fn, labels) => { const vals = [...new Set(list.flatMap(fn))]; const opts = vals.map(v => [v, labels ? labels(v) : v, cnt(fn, v)]).filter(o => o[2] > 0).sort((a, b) => b[2] - a[2]); return opts.length > 1 || (opts.length === 1 && opts[0][2] < N) ? { h, f, opts } : null; };
      const groups = [
        mk('Concern', 'concern', p => p.f ? [] : p.c.filter(c => CONCERNS[c]), v => CONCERNS[v]),
        mk('Skin / hair type', 'skin', p => p.s, v => v === 'All' ? 'All types' : v),
        mk('Key ingredient', 'ing', p => p.g),
        mk('Scent family', 'fam', p => p.f ? [p.f] : [], v => FAM[v] || v),
        mk('For', 'for', p => p.f && p.w ? [p.w] : [])
      ].filter(Boolean);
      const subs = [...new Set(list.map(p => p.t))];
      const brands = [...new Set(list.map(p => p.b))].sort((a, b) => (brandCount[b] || 0) - (brandCount[a] || 0));
      const topSubs = subs.filter(s => s !== 'More').map(s => [s, list.filter(p => p.t === s).length]).sort((a, b) => b[1] - a[1]).slice(0, 7);
      const tc = $('.typechips');
      if (tc) { tc.hidden = topSubs.length < 2; tc.innerHTML = topSubs.length < 2 ? '' : `<button data-chip="" aria-pressed="true">All ${N}</button>` + topSubs.map(([s, c]) => `<button data-chip="${esc(s)}" aria-pressed="false">${esc(s)} <small>${c}</small></button>`).join(''); }
      const opt = (f, v, label, i, c) => `<label class="${i >= 8 ? 'extra' : ''}"><input type="checkbox" data-f="${f}" value="${esc(v)}">${esc(label)}${c != null ? ` <small style="margin-left:auto">${c}</small>` : ''}</label>`;
      $('#filters').innerHTML = `<div><h2>Type</h2><div class="opts">${subs.map((s, i) => opt('sub', s, s, i)).join('')}</div>${subs.length > 8 ? `<button class="showall" data-showall>Show all ${subs.length}</button>` : ''}</div>
      <div><h2>Brand</h2><div class="opts">${brands.map((b, i) => opt('brand', b, b, i, list.filter(p => p.b === b).length)).join('')}</div>${brands.length > 8 ? `<button class="showall" data-showall>Show all ${brands.length} brands</button>` : ''}</div>
      ${groups.map(g => `<div><h2>${g.h}</h2><div class="opts">${g.opts.map((o, i) => opt(g.f, o[0], o[1], i, o[2])).join('')}</div>${g.opts.length > 8 ? `<button class="showall" data-showall>Show all ${g.opts.length}</button>` : ''}</div>`).join('')}
      <div><h2>Price</h2>${[['0-20', 'Under £20'], ['20-50', '£20 – £50'], ['50-100', '£50 – £100'], ['100-9999', 'Over £100']].map(([v, l]) => `<label><input type="checkbox" data-f="price" value="${v}">${l}</label>`).join('')}</div>
      <div><h2>Availability</h2><label><input type="checkbox" data-f="stock" value="1">In stock only</label></div>`;
    }
    function apply(reset) {
      let list = [...all];
      const sel = f => $$(`#filters input[data-f="${f}"]:checked`).map(i => i.value);
      const subs = sel('sub'), brs = sel('brand'), prs = sel('price'), stock = sel('stock').length, con = sel('concern'), sk = sel('skin'), ig = sel('ing'), fm = sel('fam'), fw = sel('for');
      if (con.length) list = list.filter(p => con.some(c => p.c.includes(c)));
      if (sk.length) list = list.filter(p => sk.some(v => p.s.includes(v)));
      if (ig.length) list = list.filter(p => ig.some(v => p.g.includes(v)));
      if (fm.length) list = list.filter(p => p.f && fm.includes(p.f));
      if (fw.length) list = list.filter(p => p.f && fw.includes(p.w));
      $$('.typechips [data-chip]').forEach(b => b.setAttribute('aria-pressed', String(subs.length ? subs.length === 1 && b.dataset.chip === subs[0] : b.dataset.chip === '')));
      if (subs.length) list = list.filter(p => subs.includes(p.t));
      if (brs.length) list = list.filter(p => brs.includes(p.b));
      if (prs.length) list = list.filter(p => prs.some(r => { const [a, b] = r.split('-').map(Number); return p.p >= a && p.p < b; }));
      if (stock) list = list.filter(p => p.ok);
      const s = $('#sort').value;
      if (s === 'feat' && brandMode) list.sort((a, b) => (b.ok - a.ok) || (a.i - b.i));
      if (s === 'low') list.sort((a, b) => a.p - b.p); if (s === 'high') list.sort((a, b) => b.p - a.p); if (s === 'az') list.sort((a, b) => a.n.localeCompare(b.n));
      const act = $('#active');
      if (act) { const on = $$('#filters input:checked'); act.hidden = !on.length;
        act.innerHTML = on.map(i => `<button data-unf="${esc(i.dataset.f)}|${esc(i.value)}">${esc(i.nextSibling.textContent.trim())} <span aria-hidden="true">×</span><span class="sr">Remove filter</span></button>`).join('') + (on.length > 1 ? '<button class="clear" data-unf="*">Clear all</button>' : ''); }
      if (reset) shown = PAGE;
      all.forEach(p => { p.el.hidden = true; });
      list.slice(0, shown).forEach(p => { p.el.hidden = false; pool.appendChild(p.el); });
      const res = $('#results'); res.querySelector('.more')?.remove(); res.querySelector('.none')?.remove();
      if (!list.length) res.insertAdjacentHTML('beforeend', '<p class="none" style="color:var(--ink-2);padding:40px 0">No products match these filters.</p>');
      else if (list.length > shown) res.insertAdjacentHTML('beforeend', `<div class="more"><span>Showing ${shown} of ${list.length}</span><button class="btn" id="loadMore">Load more</button></div>`);
      $('#count').textContent = list.length; syncHearts();
    }
    root.addEventListener('change', e => { if (e.target.closest('#filters') || e.target.id === 'sort') apply(true); });
    document.addEventListener('click', e => {
      const chip = e.target.closest('[data-chip]'); if (chip) { $$('#filters input[data-f="sub"]').forEach(i => { i.checked = chip.dataset.chip !== '' && i.value === chip.dataset.chip; }); apply(true); return; }
      const unf = e.target.closest('[data-unf]'); if (unf) { const [f, v] = unf.dataset.unf.split('|'); $$('#filters input:checked').forEach(i => { if (f === '*' || (i.dataset.f === f && i.value === v)) i.checked = false; }); apply(true); return; }
      const sa = e.target.closest('[data-showall]'); if (sa) { const o = sa.previousElementSibling; const open = o.classList.toggle('all'); if (open) sa.dataset.label = sa.dataset.label || sa.textContent; sa.textContent = open ? 'Show fewer' : sa.dataset.label; return; }
      if (e.target.closest('#loadMore')) { shown += PAGE; apply(false); return; }
      if (e.target.closest('#ftoggle')) $('#filters').classList.toggle('open');
    });
    collect(); build(); if (brandMode) apply(true);
    const pages = +root.dataset.pages || 1;
    if (pages > 1) (async () => { for (let n = 2; n <= pages; n++) { const html = await (await fetch(`${root.dataset.url}?page=${n}&section_id=${root.dataset.section}`)).text();
      const d = new DOMParser().parseFromString(html, 'text/html'); $$('#sw-pool article.p-card', d).forEach(a => { a.hidden = true; pool.appendChild(document.importNode(a, true)); }); }
      collect(); build(); if (brandMode) apply(false); })();
  })();

  /* ---------- product page (productPage() handlers) ---------- */
  (() => {
    const root = $('[data-pdp]'); const seenKey = 'swansura-seen'; let seen = store.get(seenKey, []);
    const cur = root ? root.dataset.handle : null;
    /* recently viewed: product pages + homepage section, cards from the sw-p-card-one section */
    const sec = $('#seenSec'), grid = $('#seenGrid');
    if (sec && grid) {
      const list = seen.filter(h => h !== cur).slice(0, 4);
      if (list.length) Promise.all(list.map(h => fetch(`/products/${encodeURIComponent(h)}?section_id=sw-p-card-one`).then(r => r.ok ? r.text() : '').catch(() => '')))
        .then(hs => { const html = hs.map(h => { const m = h.match(/<article[\s\S]*<\/article>/); return m ? m[0] : ''; }).join(''); if (html) { grid.innerHTML = html; sec.hidden = false; syncHearts(); } });
    }
    if (!root) return;
    store.set(seenKey, [cur, ...seen.filter(h => h !== cur)].slice(0, 12));
    const V = JSON.parse($('#sw-variants')?.textContent || '{}'), vars = V.variants || [];
    let v = vars.find(x => x.id == ($('[data-addq]')?.dataset.addq)) || vars[0];
    const keep = 1 - (V.save || 0);
    const setVariant = id => {
      v = vars.find(x => x.id == id) || v;
      $$('[data-addq]').forEach(b => b.dataset.addq = v.id); $$('[data-buynow]').forEach(b => b.dataset.buynow = v.id);
      const sb = $('#stickybar [data-add]'); if (sb) sb.dataset.add = v.id;
      const sp = $('[data-sticky-price]'); if (sp) sp.textContent = money(v.price);
      const pr = $('#pdpPrice'); if (pr) pr.innerHTML = money(v.price) + (v.compare > v.price ? ` <s>${money(v.compare)}</s> <span class="off">SAVE ${100 - Math.round(v.price * 100 / v.compare)}%</span>` : '');
      const pl = $('#payLater'); if (pl) { pl.hidden = !(v.ok && v.price >= 3000 && v.price <= 200000); pl.querySelector('b').textContent = money(Math.floor(v.price / 3)); }
      const one = $('[data-pk="1"]'), two = $('[data-pk="2"]'), each = $('[data-pk="each"]');
      if (one) one.textContent = money(v.price);
      if (two) two.textContent = money(V.live ? Math.round(v.price * 2 * keep) : v.price * 2);
      if (each) each.textContent = money(V.live ? Math.round(v.price * keep) : v.price);
      const u = new URL(location.href); u.searchParams.set('variant', v.id); history.replaceState(null, '', u);
    };
    document.addEventListener('change', e => { if (e.target.name === 'variant') setVariant(e.target.value); });
    /* ingredients: inciBlock() */
    $$('[data-inci]').forEach(box => {
      const d = JSON.parse(box.querySelector('script').textContent), inci = d.inci || [], heroes = d.heroes || [], id = box.dataset.id; if (!inci.length) return;
      const GEN = /^(milk|water|extract|oil|oils|butter|powder|seed|leaf|flower|root|juice|proteins?|natural|pure|fresh|organic)$/;
      const hk = heroes.map(h => h.toLowerCase().split(/[\s&,]+/).filter(w => w.length >= 4 && !GEN.test(w))).filter(ws => ws.length).map(ws => new RegExp(`\\b(${ws.map(w => w.replace(/[^a-z0-9]/g, '')).join('|')})`, 'i'));
      const isHero = n => hk.some(re => re.test(n));
      const split = n => { const m = n.match(/^(.+?)\s*\(([^()]*)\)$/); return m ? [m[1], m[2]] : [n, '']; };
      const g = Object.assign({}, ...inci.map(c => c.g)), lab = (c, m) => c.g[m] || g[m] || (m === 1 || m === '1' ? 'Organic' : 'Plant derived');
      const ck = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>';
      const panel = (c, k) => { const cnt = {}; c.l.forEach(([, m]) => { if (m) cnt[m] = (cnt[m] || 0) + 1; });
        return `<div class="inci-panel" role="tabpanel" id="inci-${id}-${k}"${k ? ' hidden' : ''}>
      <div class="inci-meta"><b>${c.l.length} ingredient${c.l.length > 1 ? 's' : ''}</b>${Object.entries(cnt).map(([m, n]) => `<span class="st"><i class="mk m${m}"></i>${n} ${esc(lab(c, m).toLowerCase())}</span>`).join('')}<button class="inci-copy" data-incicopy="${esc(c.l.map(x => x[0]).join(', '))}">${ck}<span>Copy list</span></button></div>
      <p class="inci-flow${c.l.length > 14 ? ' clip' : ''}">${c.l.map(([n, m]) => { const [main, sub] = split(n), h = isHero(n); return `<span class="ii${h ? ' hi' : ''}">${esc(main)}${sub ? ` <small>(${esc(sub)})</small>` : ''}${m ? `<i class="mk m${m}" title="${esc(lab(c, m))}" aria-label="${esc(lab(c, m))}"></i>` : ''}</span>`; }).join('<span class="sep" aria-hidden="true">·</span>')}</p>
      ${c.l.length > 14 ? `<button class="inci-more" data-incimore aria-expanded="false">Show all ${c.l.length} ingredients</button>` : ''}
    </div>`; };
      box.innerHTML = `<div class="inci"><div class="inci-head"><h3>Full ingredient list</h3>
      <div class="inci-legend">${hk.length ? '<span class="lg-hero"><i></i>Hero ingredient</span>' : ''}${Object.keys(g).map(m => `<span><i class="mk m${m}"></i>${esc(g[m])}</span>`).join('')}</div></div>
    <p class="inci-intro">As listed by ${esc(box.dataset.brand)}, from the highest to the lowest amount.${inci.length > 1 ? (/^Step \d/.test(inci[0].n) ? ` Used in ${inci.length} steps.` : ` This kit has ${inci.length} products.`) : ''}</p>
    ${inci.length > 1 ? `<div class="inci-tabs" role="tablist" aria-label="Products in this kit">${inci.map((c, k) => `<button role="tab" aria-selected="${!k}" aria-controls="inci-${id}-${k}" data-incitab="${k}">${esc(c.n)}</button>`).join('')}</div>` : ''}
    ${inci.map(panel).join('')}
    <p class="inci-note">Always check the pack for the most up-to-date list, and patch test before first use.</p></div>`;
    });
    document.addEventListener('click', async e => {
      const it = e.target.closest('[data-incitab]');
      if (it) { const s = it.closest('.inci'); $$('[data-incitab]', s).forEach(b => b.setAttribute('aria-selected', b === it)); $$('.inci-panel', s).forEach((p, k) => p.hidden = k !== +it.dataset.incitab); return; }
      const m = e.target.closest('[data-incimore]');
      if (m) { const l = m.previousElementSibling, clipped = l.classList.toggle('clip'); m.setAttribute('aria-expanded', !clipped); m.textContent = clipped ? `Show all ${l.querySelectorAll('.ii').length} ingredients` : 'Show fewer'; return; }
      const c = e.target.closest('[data-incicopy]');
      if (c) { const done = () => { c.querySelector('span').textContent = 'Copied'; setTimeout(() => c.querySelector('span').textContent = 'Copy list', 1800); };
        try { navigator.clipboard.writeText(c.dataset.incicopy).then(done, () => toast('Select the list to copy it')); } catch (err) { toast('Select the list to copy it'); } return; }
      const rv = e.target.closest('[data-review]');
      if (rv) { const w = $('#judgeme_product_reviews'); if (w) { w.hidden = false; const l = w.querySelector('.jdgm-write-rev-link'); if (l) l.click(); else w.scrollIntoView({ behavior: 'smooth' }); } return; }
      const t = e.target.closest('[data-frame],[data-q],[data-jump],[data-addq],[data-buynow]'); if (!t) return;
      if (t.dataset.frame) { const img = $('#mainImg img'); if (img) { img.srcset = t.dataset.srcset; img.src = t.dataset.full; img.alt = t.dataset.alt; } $$('button', t.parentElement).forEach(b => b.setAttribute('aria-current', b === t)); return; }
      if (t.dataset.q) { const o = $('#qty'); o.value = o.textContent = Math.max(1, (+o.textContent) + (+t.dataset.q)); return; }
      if (t.dataset.jump) { e.preventDefault(); const el = document.getElementById(t.dataset.jump); if (el) { if (el.tagName === 'DETAILS') el.open = true; el.scrollIntoView({ behavior: 'smooth' }); } return; }
      e.preventDefault(); const bn = !!t.dataset.buynow, q = +($('#qty')?.textContent || 1), pk = $('input[name="pack"]:checked')?.value || 'single';
      let items = [{ id: +v.id, quantity: q }];
      if (pk === 'duo') items = [{ id: +v.id, quantity: 2 * q }];
      else if (pk === 'routine') { const ids = ($('.complete [data-addall]')?.dataset.addall || '').split(',').filter(Boolean); ids[0] = v.id; items = ids.map(id => ({ id: +id, quantity: q })); }
      t.disabled = true; const ok = await addItems(items); t.disabled = false; if (!ok) return;
      if (bn) { location.href = '/checkout'; return; }
      const msg = pk === 'duo' ? (V.live ? `Duo added · ${Math.round(V.save * 100)}% pack saving applied at checkout` : 'Duo added to your bag')
        : pk === 'routine' ? (V.live ? `Routine added · ${Math.round(V.save * 100)}% pack saving applied at checkout` : 'Routine added to your bag') : '';
      await added(String(v.id), msg);
    });
  })();

  /* ---------- wishlist page (wishlistPage()) ---------- */
  (() => {
    const g = $('#wishGrid'); if (!g) return;
    const list = store.get('swansura-wish', []), lede = $('#wishLede'), empty = $('#wishEmpty');
    if (!list.length) return;
    lede.textContent = `${list.length} saved product${list.length > 1 ? 's' : ''}.`;
    Promise.all(list.map(h => fetch(`/products/${encodeURIComponent(h)}?section_id=sw-p-card-one`).then(r => r.ok ? r.text() : '').catch(() => '')))
      .then(hs => { const html = hs.map(h => { const m = h.match(/<article[\s\S]*<\/article>/); return m ? m[0] : ''; }).join('');
        if (html) { g.innerHTML = html; g.hidden = false; empty.hidden = true; syncHearts(); } });
  })();

  /* ---------- advent doors (adventPage()): opened doors are remembered in this browser ---------- */
  (() => {
    if (!$('[data-door]')) return;
    let opened = store.get('swansura-advent', {});
    const paint = d => { const on = !!opened[d.dataset.door], t = d.querySelector('template');
      if (on && !d.classList.contains('open')) { d.dataset.closed = d.dataset.closed || d.innerHTML.replace(/<template[\s\S]*<\/template>/, ''); d.innerHTML = t.innerHTML + t.outerHTML; d.classList.add('open'); d.setAttribute('aria-label', d.dataset.label); }
      else if (!on && d.classList.contains('open')) { d.innerHTML = d.dataset.closed + t.outerHTML; d.classList.remove('open'); d.setAttribute('aria-label', d.dataset.label.split(':')[0]); } };
    $$('[data-door]').forEach(paint);
    document.addEventListener('click', e => {
      const d = e.target.closest('[data-door]'); if (d) { opened[d.dataset.door] = !opened[d.dataset.door]; store.set('swansura-advent', opened); paint(d); return; }
      const r = e.target.closest('[data-revealall]'); if (!r) return;
      const ds = $$(`[data-doors="${r.dataset.revealall}"] [data-door]`), all = ds.every(x => opened[x.dataset.door]);
      ds.forEach(x => { opened[x.dataset.door] = !all; paint(x); }); store.set('swansura-advent', opened);
    });
  })();

  syncHearts(); getCart().catch(() => {});
})();
