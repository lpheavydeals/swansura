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
})();
