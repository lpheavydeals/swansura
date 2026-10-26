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
  const pic = (src, alt) => src ? `<img class="pic" src="${esc(src)}${src.includes('?') ? '&' : '?'}width=200" alt="${esc(alt)}" loading="lazy" width="200" height="250">` : '<div class="pic"></div>';
  async function openBag(justAdded) {
    await getCart();
    const total = cart.total_price / 100, ng = nextGoal(total);
    const inBag = new Set(cart.items.map(i => i.variant_id));
    const extras = (cfg.extras || []).filter(x => !inBag.has(x.id)).sort((a, b) => a.price - b.price).slice(0, 6);
    const lines = cart.items.length ? cart.items.map(l => `<div class="line${l.variant_id == justAdded ? ' just' : ''}">${pic(l.image, l.product_title)}<div><div style="font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--brass-ink)">${esc(l.vendor)}</div><a href="${esc(l.url)}" data-close>${esc(l.product_title)}${l.variant_title && !/default/i.test(l.variant_title) ? ' · ' + esc(l.variant_title) : ''}</a><div class="bq"><div class="qty sm"><button data-bq="${esc(l.key)}|${l.quantity - 1}" aria-label="Decrease quantity">−</button><span>${l.quantity}</span><button data-bq="${esc(l.key)}|${l.quantity + 1}" aria-label="Increase quantity">+</button></div><button class="rm" data-bq="${esc(l.key)}|0">Remove</button></div></div><div>${money(l.final_line_price)}</div></div>`).join('')
      : `<div class="bag-empty"><p>Your bag is empty.</p><a class="btn solid" href="/collections/all" data-close>Shop bestsellers</a><a class="p-link" href="/collections/sets-combos" data-close>Or start with a routine</a></div>`;
    const discount = cart.total_discount > 0 ? `<div style="display:flex;justify-content:space-between;font-size:14px;color:var(--emerald)"><span>Savings</span><b>−${money(cart.total_discount)}</b></div>` : '';
    openLayer(`<div class="scrim" data-close></div>
  <div class="bag" role="dialog" aria-modal="true" aria-label="Your bag">
    <div class="bag-head"><h3>Your bag</h3><button data-close aria-label="Close bag">Close</button></div>
    <div class="lines">${lines}</div>
    <div class="foot">
      <div class="delivery" style="border:0;padding:0;background:none"><span>${ng ? `You're <b>£${ng.left.toFixed(2)}</b> away from ${ng.what}${total >= offers.delivery ? ' (free UK delivery unlocked)' : ''}` : `<b>Free UK delivery + £${offers.bonus.off} off unlocked</b> (applied at checkout)`}</span><div class="bar"><i style="width:${Math.min(100, total / (ng ? ng.goal : 1) * 100)}%"></i></div></div>
      ${extras.length ? `<div><div class="eyebrow" style="margin-bottom:8px">Little extras</div><div class="extras">${extras.map(x => `<div class="extra">${pic(x.img, x.title)}<span>${esc(x.title)}</span><b>${money(x.price)}</b><button data-add="${x.id}">Add</button></div>`).join('')}</div></div>` : ''}
      ${discount}<div style="display:flex;justify-content:space-between;font-size:16px"><span>Subtotal</span><b>${money(cart.total_price)}</b></div>
      <p class="bag-note">Taxes included. Discount codes and delivery are added at checkout.</p>
      <a class="btn solid" id="checkoutBtn" href="/checkout"${cart.items.length ? '' : ' aria-disabled="true" style="pointer-events:none;opacity:.5"'}>Checkout securely</a>
      <div class="bag-trust"><span>${icon.truck} Dispatched in 1–2 days</span><span>${icon.ret} <a href="${esc(cfg.returnsUrl || '/policies/refund-policy')}" data-close>Returns policy</a></span><span>${icon.lock} Secure checkout</span></div>
      <span class="pays" aria-label="Payment methods">${(cfg.pays || []).map(x => `<span class="pay">${esc(x)}</span>`).join('')}</span>
    </div>
  </div>`);
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
    const nt = e.target.closest('[data-notify]'); if (nt) { toast('Thanks. We will email you when the ' + (nt.dataset.notify === 'skin' ? 'Skin' : 'Scent') + ' Studio Advent launches'); return; }
    const t = e.target.closest('[data-add],[data-addall],[data-bq],[data-close],[data-tab],#openBag,#openSearch,#burger,#drawerSearch');
    if (!t) { if (e.target.closest('.drawer-nav a')) closeLayer(); return; }
    if (t.dataset.add) { e.preventDefault(); if (t.classList.contains('add')) burst(t); t.disabled = true;
      if (await addItems([{ id: +t.dataset.add, quantity: 1 }])) await openBag(t.dataset.add); t.disabled = false; return; }
    if (t.dataset.addall) { e.preventDefault(); if (await addItems(t.dataset.addall.split(',').map(id => ({ id: +id, quantity: 1 })))) { toast('Ritual added to your bag'); await openBag(); } return; }
    if (t.dataset.bq) { const [key, q] = t.dataset.bq.split('|'); await change(key, Math.max(0, +q)); await openBag(); return; }
    if ('close' in t.dataset) { if (t.tagName !== 'A') e.preventDefault(); closeLayer(); return; }
    if (t.dataset.tab) { $$('.tabs [data-tab]').forEach(b => b.setAttribute('aria-selected', b === t)); const g = $('#bestGrid'), src = $('#best-' + t.dataset.tab); if (g && src) { g.innerHTML = src.innerHTML; syncHearts(); } return; }
    if (t.id === 'openBag') { e.preventDefault(); openBag(); return; }
    if (t.id === 'openSearch') { e.preventDefault(); openSearch(); return; }
    if (t.id === 'burger') { const tp = $('#sw-drawer-tpl'); if (tp) openLayer(tp.innerHTML); return; }
    if (t.id === 'drawerSearch') { closeLayer(); openSearch(); }
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && layer()?.innerHTML) closeLayer(); });

  /* ---------- announcement bar: one message at a time where they don't fit side by side ---------- */
  (() => { const items = $$('.announce .wrap>*'); if (items.length < 2) return; let i = 0; items[0].classList.add('on');
    setInterval(() => { items[i].classList.remove('on'); i = (i + 1) % items.length; items[i].classList.add('on'); }, 1000); })();

  /* ---------- hero: skin + scent pairs slide together ---------- */
  (() => { const st = $('.hero .stage'); if (!st) return; const tracks = $$('.track', st), n = tracks[0]?.children.length || 0; let i = 0, timer;
    const go = k => { i = (k + n) % n; tracks.forEach(t => { t.style.transform = `translateX(-${i * 100}%)`; [...t.children].forEach((a, j) => { a.tabIndex = j === i ? 0 : -1; a.setAttribute('aria-hidden', j !== i); }); }); };
    const play = () => { clearInterval(timer); if (!reduce && n > 1) timer = setInterval(() => go(i + 1), 1000); };
    st.onmouseenter = st.onfocusin = () => clearInterval(timer); st.onmouseleave = st.onfocusout = play;
    let x0 = null; st.ontouchstart = e => { x0 = e.touches[0].clientX; clearInterval(timer); };
    st.ontouchend = e => { if (x0 != null) { const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) go(i + (dx < 0 ? 1 : -1)); x0 = null; } play(); };
    go(0); play(); })();

  /* ---------- help / chat panel ---------- */
  (() => { const b = $('#chatBtn'), p = $('#chatPanel'); if (!b || !p) return; const set = open => { p.hidden = !open; b.setAttribute('aria-expanded', open); if (open) p.querySelector('a').focus(); };
    b.addEventListener('click', () => set(p.hidden)); p.addEventListener('click', e => { if (e.target.closest('[data-chatclose]')) set(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !p.hidden) { set(false); b.focus(); } }); })();

  syncHearts(); getCart().catch(() => {});
})();
