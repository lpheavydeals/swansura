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
  const pic = (src, alt) => src ? `<img class="pic" src="${esc(src)}${src.includes('?') ? '&' : '?'}width=200" alt="${esc(alt)}" width="200" height="250">` : '<div class="pic"></div>';
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

  syncHearts(); getCart().catch(() => {});
})();
