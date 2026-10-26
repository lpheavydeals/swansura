/* Swansura theme behaviour: announcement rotation, hero slider, product tabs. No dependencies. */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Announcement: one message at a time up to 1320px (all side by side above). */
  document.querySelectorAll('[data-sw-rotate]').forEach(bar => {
    const items = [...bar.querySelectorAll('.sw-announce__msg')];
    if (items.length < 2) return;
    let i = 0;
    setInterval(() => {
      if (!matchMedia('(max-width: 1320px)').matches) return;
      items[i].classList.remove('is-on');
      i = (i + 1) % items.length;
      items[i].classList.add('is-on');
    }, Number(bar.dataset.swRotate) || 1000);
  });

  /* Hero: arch + card slide together; pauses on hover/focus/touch; swipe on phones; still with reduced motion. */
  document.querySelectorAll('[data-sw-hero]').forEach(stage => {
    const tracks = [...stage.querySelectorAll('.sw-hero__track')];
    const n = tracks[0] ? tracks[0].children.length : 0;
    if (n < 2) return;
    let i = 0, paused = false, x0 = null;
    const go = k => {
      i = (k + n) % n;
      tracks.forEach(t => {
        t.style.transform = `translateX(-${i * 100}%)`;
        [...t.children].forEach((a, j) => a.tabIndex = j === i ? 0 : -1);
      });
    };
    ['mouseenter', 'focusin', 'touchstart'].forEach(e => stage.addEventListener(e, () => paused = true, { passive: true }));
    ['mouseleave', 'focusout'].forEach(e => stage.addEventListener(e, () => paused = false));
    stage.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', e => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) go(i + (dx < 0 ? 1 : -1));
      setTimeout(() => paused = false, 3000);
    });
    if (!reduce) setInterval(() => { if (!paused && !document.hidden) go(i + 1); }, Number(stage.dataset.interval) || 1000);
  });

  /* Tabs */
  document.querySelectorAll('[data-sw-tabs]').forEach(sec => {
    const tabs = [...sec.querySelectorAll('[role="tab"]')];
    tabs.forEach(t => t.addEventListener('click', () => {
      tabs.forEach(o => {
        const on = o === t;
        o.setAttribute('aria-selected', on);
        const panel = sec.querySelector('#' + o.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
    }));
  });

  /* ---------- Product pages ---------- */
  const gbp = p => new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' }).format(p / 100);

  /* Free-delivery progress: refresh from /cart.js whenever the bag changes. */
  const goals = [...document.querySelectorAll('[data-sw-goal]')];
  const paintGoal = total => goals.forEach(g => {
    const free = +g.dataset.free, bonus = +g.dataset.bonus;
    const txt = g.querySelector('[data-sw-goal-text]'), bar = g.querySelector('[data-sw-goal-bar]');
    if (txt) txt.textContent = total >= bonus ? 'Your bag gets free UK delivery and £5 off.'
      : total >= free ? `Free UK delivery unlocked. Spend ${gbp(bonus - total)} more for £5 off.`
      : total > 0 ? `Spend ${gbp(free - total)} more for free UK delivery.`
      : 'Free UK delivery over £40 · free delivery + £5 off over £70';
    if (bar) bar.style.width = Math.min(100, total * 100 / bonus) + '%';
  });
  const refreshGoal = () => goals.length && fetch('/cart.js').then(r => r.json()).then(c => paintGoal(c.total_price)).catch(() => {});

  /* Variant change: PayPal Pay in 3 line (£30–£2,000) and sticky bar price. */
  const onVariant = v => {
    if (!v) return;
    document.querySelectorAll('[data-sw-paylater]').forEach(el => {
      el.hidden = v.price < 3000 || v.price > 200000;
      const amt = el.querySelector('[data-sw-paylater-amount]');
      if (amt) amt.textContent = gbp(Math.round(v.price / 3));
    });
    const sp = document.querySelector('[data-sw-sticky-price]');
    if (sp) sp.textContent = gbp(v.price);
    const sb = document.querySelector('[data-sw-sticky-btn]');
    if (sb) { sb.disabled = !v.available; sb.textContent = v.available ? 'Add to cart' : 'Sold out'; }
  };

  /* Sticky Add-to-bag bar: shows once the main button is off screen; clicks the main submit button. */
  const sticky = document.querySelector('[data-sw-sticky]');
  const mainBtn = document.querySelector('product-info product-form button[type="submit"], product-form button[name="add"]');
  if (sticky && mainBtn && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => {
      const show = !e.isIntersecting && e.boundingClientRect.top < 0;
      sticky.hidden = !show;
      document.body.classList.toggle('sw-has-sticky', show);
    }).observe(mainBtn);
    sticky.querySelector('[data-sw-sticky-btn]').addEventListener('click', () => {
      mainBtn.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
      mainBtn.click();
    });
  }

  /* Recently viewed: remember up to 12 handles in this browser; show the others as small cards. */
  document.querySelectorAll('[data-sw-recent]').forEach(sec => {
    const key = 'sw-recent', cur = sec.dataset.current, limit = +sec.dataset.limit || 6;
    let list = [];
    try { list = JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) {}
    if (cur) {
      try { localStorage.setItem(key, JSON.stringify([cur, ...list.filter(h => h !== cur)].slice(0, 12))); } catch (e) {}
    }
    const show = list.filter(h => h !== cur).slice(0, limit);
    if (!show.length) return;
    const ul = sec.querySelector('[data-sw-recent-list]');
    Promise.all(show.map(h => fetch(`/products/${h}.js`).then(r => r.ok ? r.json() : null).catch(() => null))).then(ps => {
      ps = ps.filter(Boolean);
      if (!ps.length) return;
      ul.innerHTML = ps.map(p => {
        const img = p.featured_image ? `<img src="${p.featured_image}${p.featured_image.includes('?') ? '&' : '?'}width=360" alt="" loading="lazy" width="360" height="450">` : '';
        const t = String(p.title).split(' – ')[0].replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
        return `<li><a href="${p.url}">${img}<span>${t}</span><b>${gbp(p.price)}</b></a></li>`;
      }).join('');
      sec.hidden = false;
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    if (typeof subscribe === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
      subscribe(PUB_SUB_EVENTS.variantChange, e => onVariant(e.data && e.data.variant));
      subscribe(PUB_SUB_EVENTS.cartUpdate, refreshGoal);
    }
  });
})();
