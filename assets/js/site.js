/* ==========================================================================
   Euroceramiche — script comune
   CONFIG: l'unico punto da modificare con i dati del negozio.
   ========================================================================== */
const CONFIG = {
  whatsapp: '393203513244',              // cellulare usato per WhatsApp (verificare)
  phone: '+39 0933 953210',
  mobile: '+39 320 351 3244',
  email: 'infoeuroceramiche@gmail.com',
  mapsQuery: 'Euroceramiche, Via Paolo VI 23, 93015 Niscemi CL',
  formEndpoint: ''                       // opzionale: URL Formspree/Netlify per ricevere anche i dati via POST
};

(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const wa = text => `https://wa.me/${CONFIG.whatsapp}${text ? '?text=' + encodeURIComponent(text) : ''}`;

  /* Link da CONFIG */
  $$('[data-wa]').forEach(a => a.href = wa(a.dataset.wa));
  $$('[data-tel="phone"]').forEach(a => a.href = 'tel:' + CONFIG.phone.replace(/\s/g, ''));
  $$('[data-tel="mobile"]').forEach(a => a.href = 'tel:' + CONFIG.mobile.replace(/\s/g, ''));
  $$('[data-mail]').forEach(a => a.href = 'mailto:' + CONFIG.email);
  $$('[data-maps]').forEach(a => a.href = 'https://www.google.com/maps/dir/?api=1&destination=' + encodeURIComponent(CONFIG.mapsQuery));
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  /* Header e menu */
  const header = $('.header'), nav = $('#nav'), btn = $('.menu-btn');
  const onScroll = () => header.classList.toggle('is-scrolled', scrollY > 4);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const setMenu = open => {
    nav.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', open);
    btn.setAttribute('aria-label', open ? 'Chiudi il menu' : 'Apri il menu');
    document.body.style.overflow = open ? 'hidden' : '';
  };
  btn?.addEventListener('click', () => setMenu(!nav.classList.contains('is-open')));
  nav?.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape' && nav?.classList.contains('is-open')) { setMenu(false); btn.focus(); } });
  matchMedia('(min-width: 1081px)').addEventListener('change', () => setMenu(false));

  /* Slider dell'hero: frecce, pausa, stop su hover/focus, niente autoplay con riduzione movimento */
  const slider = $('[data-slider]');
  if (slider) {
    const slides = $$('.slide', slider), num = $('[data-slide-num]', slider), pauseBtn = $('[data-slide-pause]', slider);
    let i = 0, timer = null, paused = reduce, hold = false;
    const show = n => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => { s.classList.toggle('is-active', k === i); s.setAttribute('aria-hidden', k !== i); });
      num.textContent = String(i + 1).padStart(2, '0');
    };
    const tick = () => { clearInterval(timer); if (!paused && !hold) timer = setInterval(() => show(i + 1), 6000); };
    const setPaused = p => {
      paused = p;
      pauseBtn.setAttribute('aria-label', p ? 'Avvia la presentazione' : 'Metti in pausa la presentazione');
      pauseBtn.innerHTML = p ? '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>' : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3v14H7zM14 5h3v14h-3z" fill="currentColor"/></svg>';
      tick();
    };
    $('[data-slide-prev]', slider).addEventListener('click', () => { show(i - 1); tick(); });
    $('[data-slide-next]', slider).addEventListener('click', () => { show(i + 1); tick(); });
    pauseBtn.addEventListener('click', () => setPaused(!paused));
    ['mouseenter', 'focusin'].forEach(ev => slider.addEventListener(ev, () => { hold = true; tick(); }));
    ['mouseleave', 'focusout'].forEach(ev => slider.addEventListener(ev, () => { hold = false; tick(); }));
    document.addEventListener('visibilitychange', () => { hold = document.hidden; tick(); });
    show(0); setPaused(paused);
  }

  /* Orari: aperto/chiuso sull'ora italiana */
  const rows = $$('.hours tr[data-day]');
  if (rows.length) {
    const DAYS = ['domenica', 'lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato'];
    const toMin = t => { const [h, m] = t.split(':').map(Number); return h * 60 + m; };
    const fmt = m => `${Math.floor(m / 60)}:${String(m % 60).padStart(2, '0')}`;
    const sched = {};
    rows.forEach(r => sched[r.dataset.day] = r.dataset.hours ? r.dataset.hours.split(',').map(x => x.split('-').map(toMin)) : []);
    const update = () => {
      const p = Object.fromEntries(new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Rome', weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date()).map(x => [x.type, x.value]));
      const day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(p.weekday), min = +p.hour * 60 + +p.minute;
      const today = sched[day] || [], slot = today.find(([a, b]) => min >= a && min < b);
      let text;
      if (slot) text = `Aperto ora · chiude alle ${fmt(slot[1])}`;
      else {
        const later = today.find(([a]) => a > min);
        if (later) text = `Chiuso · riapre alle ${fmt(later[0])}`;
        else for (let k = 1; k <= 7; k++) { const d = (day + k) % 7; if (sched[d]?.length) { text = `Chiuso · riapre ${k === 1 ? 'domani' : DAYS[d]} alle ${fmt(sched[d][0][0])}`; break; } }
      }
      $$('[data-status]').forEach(el => { el.dataset.open = !!slot; $('span', el).textContent = text; });
      rows.forEach(r => r.classList.toggle('is-today', +r.dataset.day === day));
    };
    update(); setInterval(update, 60000);
  } else {
    // pagine senza tabella: stato calcolato con gli orari standard del negozio
    const std = { 1: [[480, 780], [900, 1200]], 2: [[480, 780], [900, 1200]], 3: [[480, 780], [900, 1200]], 4: [[480, 780], [900, 1200]], 5: [[480, 780], [900, 1200]], 6: [[480, 780], [900, 1140]], 0: [] };
    const p = Object.fromEntries(new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Rome', weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date()).map(x => [x.type, x.value]));
    const day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(p.weekday), min = +p.hour * 60 + +p.minute;
    const open = (std[day] || []).some(([a, b]) => min >= a && min < b);
    $$('[data-status]').forEach(el => { el.dataset.open = open; $('span', el).textContent = open ? 'Showroom aperto ora' : 'Showroom chiuso ora'; });
  }


  /* ---------- Effetti di ingresso e di scroll ---------- */
  const root = document.documentElement;
  // titoli brevi (≤ 8 parole) parola per parola, conservando <strong>; testo intero per gli screen reader
  $$('h1, .head h2, .intro-text h2, .prose h2, .band h2, .quote-aside h2').forEach(h => {
    const words = h.textContent.trim().split(/\s+/);
    if (words.length > 8 || reduce) return;
    h.setAttribute('aria-label', h.textContent.replace(/\s+/g, ' ').trim());
    let k = 0;
    const wrap = node => [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const f = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(t => {
          if (!t) return;
          if (/^\s+$/.test(t)) { f.append(' '); return; }
          const w = document.createElement('span'); w.className = 'w'; w.setAttribute('aria-hidden', 'true');
          const i = document.createElement('span'); i.textContent = t; i.style.setProperty('--wi', k++);
          w.append(i); f.append(w);
        });
        n.replaceWith(f);
      } else if (n.nodeType === 1) wrap(n);
    });
    wrap(h); h.classList.add('words');
    if (h.matches('h1')) h.style.setProperty('--wd', '250ms');
  });
  // foto: svelamento dal basso
  $$('.frame').forEach(f => f.setAttribute('data-clip', ''));
  // celle dei marchi a cascata
  $$('.brands').forEach(u => $$('li', u).forEach((li, k) => li.style.setProperty('--bi', k)));

  const fx = new IntersectionObserver(en => en.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); fx.unobserve(e.target); } }), { rootMargin: '0px 0px -12% 0px' });
  $$('.words, [data-clip], .offset, .service, .brands').forEach(el => { if (!el.closest('.hero')) fx.observe(el); });

  // apertura: header, titolo e foto dell'hero
  const start = () => {
    root.classList.add('is-loaded');
    $$('.hero .words, .page-head .words, .hero [data-clip]').forEach(el => el.classList.add('is-in'));
  };
  if (reduce) start(); else requestAnimationFrame(() => requestAnimationFrame(start));

  // barra di avanzamento, parallasse leggera e cubo che ruota (un solo ciclo, solo se serve)
  const bar = document.createElement('div'); bar.className = 'progress'; bar.setAttribute('aria-hidden', 'true'); document.body.append(bar);
  const frames = $$('[data-clip]').filter(f => !f.closest('.hero')), cubes = $$('.band svg.cube, .quote-aside svg.cube');
  let ticking = false;
  const onFx = () => {
    ticking = false;
    const vh = innerHeight, y = scrollY;
    bar.style.setProperty('--sp', (y / Math.max(1, document.documentElement.scrollHeight - vh)).toFixed(4));
    if (reduce) return;
    frames.forEach(f => {
      const r = f.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const c = (r.top + r.height / 2 - vh / 2) / vh;          // -0.5 … 0.5 circa
      $('img', f)?.style.setProperty('--py', (c * -28).toFixed(1) + 'px');
    });
    cubes.forEach(c => c.style.setProperty('--rot', (y * .12 % 360).toFixed(1) + 'deg'));
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onFx); } }, { passive: true });
  onFx();

  /* Comparsa allo scroll */
  const io = new IntersectionObserver(en => en.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('[data-reveal]').forEach(el => io.observe(el));

  /* Toast */
  const toast = $('.toast'); let tt;
  const say = msg => { if (!toast) return; toast.textContent = msg; toast.classList.add('is-on'); clearTimeout(tt); tt = setTimeout(() => toast.classList.remove('is-on'), 4500); };

  /* Pulsanti "chiedi un preventivo per…" → modulo precompilato */
  $$('[data-quote]').forEach(b => b.addEventListener('click', () => { const f = $('#q-interesse'); if (f) f.value = b.dataset.quote; }));

  /* Modulo preventivo: etichette visibili, verifica all'uscita dal campo, errore vicino al campo */
  $$('form[data-quote-form]').forEach(form => {
    const rules = {
      nome: el => el.value.trim().length > 1,
      telefono: el => /^[0-9+ ]{6,}$/.test(el.value.trim()),
      privacy: el => el.checked
    };
    const check = el => { const ok = rules[el.name](el); el.setAttribute('aria-invalid', !ok); return ok; };
    Object.keys(rules).forEach(n => {
      const el = form.elements[n];
      el.addEventListener('blur', () => { if (el.type !== 'checkbox' && el.value) check(el); });
      el.addEventListener(el.type === 'checkbox' ? 'change' : 'input', () => { if (el.getAttribute('aria-invalid') === 'true') check(el); });
    });
    form.addEventListener('submit', e => {
      e.preventDefault();
      const bad = Object.keys(rules).map(n => form.elements[n]).filter(el => !check(el));
      if (bad.length) { bad[0].focus(); say('Controllate i campi segnati in rosso.'); return; }
      const d = new FormData(form);
      const lines = [
        ['Nome', d.get('nome')], ['Telefono', d.get('telefono')], ['Comune', d.get('comune')],
        ['Interesse', d.get('interesse')], ['Ambienti', d.getAll('ambienti').join(', ')],
        ['Metri quadri', d.get('mq')], ['Messaggio', d.get('messaggio')]
      ].filter(([, v]) => v && String(v).trim());
      const msg = 'Buongiorno, vorrei un preventivo gratuito.\n\n' + lines.map(([k, v]) => `${k}: ${String(v).trim()}`).join('\n');
      if (CONFIG.formEndpoint) fetch(CONFIG.formEndpoint, { method: 'POST', body: d, headers: { Accept: 'application/json' } }).catch(() => {});
      if (e.submitter?.value === 'email') location.href = `mailto:${CONFIG.email}?subject=${encodeURIComponent('Richiesta preventivo dal sito')}&body=${encodeURIComponent(msg)}`;
      else window.open(wa(msg), '_blank', 'noopener');
      say('Perfetto: inviate il messaggio e vi ricontattiamo al più presto.');
    });
  });
})();
