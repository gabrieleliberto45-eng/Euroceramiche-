#!/usr/bin/env python3
"""Genera le pagine del sito Euroceramiche (header, footer e modulo condivisi).

Uso:  python3 tools/build.py        (dalla cartella principale del repository)
Le pagine HTML generate vanno pubblicate così come sono: nessun build lato server.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- icone
CUBE = '<svg class="cube" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l8.5 4.7v9.6L12 21.5l-8.5-4.7V7.2z M3.5 7.2L12 12l8.5-4.8 M12 12v9.5" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>'
ICONS = {
    'arrow': '<path d="M4 12h16M14 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    'prev': '<path d="M15 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    'next': '<path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    'pause': '<path d="M7 5h3v14H7zM14 5h3v14h-3z" fill="currentColor"/>',
    'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    'mail': '<g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14"/><path d="M3 7l9 6 9-6"/></g>',
    'pin': '<g fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></g>',
    'ig': '<g fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".7" fill="currentColor"/></g>',
    'wa': '<path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1-.7-.3-1.4-.7-2-1.3-.5-.5-1-1.1-1.3-1.7-.1-.2 0-.4.1-.5l.4-.5.3-.5v-.5l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3c-.3.3-1 1-1 2.3s1 2.7 1.2 2.9c.1.2 2 3.1 4.9 4.3 1.8.7 2.5.8 3.4.7.6-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.5-.3z"/>',
    'truck': '<g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M2.5 6.5h11v9h-11zM13.5 9.5h4l3 3v3h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></g>',
    'doc': '<g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></g>',
    'chat': '<g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/></g>',
    'render': '<g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/></g>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    'star': '<path fill="currentColor" d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z"/>',
}
def ic(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

LOGO = f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l8.5 4.7v9.6L12 21.5l-8.5-4.7V7.2z M3.5 7.2L12 12l8.5-4.8 M12 12v9.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg><span><b>EUROCERAMICHE</b><small>progettare insieme</small></span>'

NAV = [('index.html', 'Home'), ('chi-siamo.html', 'Chi siamo'), ('arredo-bagno.html', 'Arredo bagno'),
       ('pavimenti-rivestimenti.html', 'Pavimenti e rivestimenti'), ('sanitari-rubinetteria.html', 'Sanitari e rubinetteria'),
       ('servizi.html', 'Servizi'), ('contatti.html', 'Contatti')]

BRANDS_BAGNO = ['Palombini', 'Royo', 'Blue Life', 'Vica', 'Eban', 'Legno Bagno', 'Global Trade', 'Progetto Idea Stella']
BRANDS_RUB = ['Carlo Frattini', 'Mamoli', 'Morini', 'Keller Taps', 'Gattoni', 'Paffoni', 'CSA', 'New Flag', 'Azzurra']
BRANDS_CER = ['Imola', 'Dado Ceramica', 'Herberia', 'FAP', 'Faetano', 'Flab']

def brands(lst):
    return '<ul class="brands">' + ''.join(f'<li>{b}</li>' for b in lst) + '</ul>'

def img(src, alt, w, h, cls='', lazy=True, srcset=None, sizes=None):
    extra = f' srcset="{srcset}" sizes="{sizes}"' if srcset else ''
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="assets/img/{src}"{extra} alt="{alt}" width="{w}" height="{h}"{load}>'

# ---------------------------------------------------------------- blocchi condivisi
def head(title, desc, extra=''):
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#faf7f3">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hero.webp">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><rect width='24' height='24' fill='%23111'/><path d='M12 4l7 3.9v8.2L12 20l-7-3.9V7.9z M5 7.9L12 12l7-4.1 M12 12v8' fill='none' stroke='%23d7b06a' stroke-width='1.4' stroke-linejoin='round'/></svg>">
<link rel="preload" href="assets/fonts/hanken-grotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
{extra}</head>
<body>
<script>(function(d){{d.classList.add('js');try{{if(sessionStorage.getItem('ec-splash')||matchMedia('(prefers-reduced-motion: reduce)').matches)d.classList.add('splash-done');else sessionStorage.setItem('ec-splash','1')}}catch(e){{}}}})(document.documentElement)</script>
<div class="splash" aria-hidden="true"><div class="splash-in"><svg class="splash-cube" viewBox="0 0 24 24"><path d="M12 2.5l8.5 4.7v9.6L12 21.5l-8.5-4.7V7.2z M3.5 7.2L12 12l8.5-4.8 M12 12v9.5" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linejoin="round"/></svg><p class="splash-name">EUROCERAMICHE</p><p class="splash-tag">progettiamo insieme</p></div></div>
<a class="skip" href="#main">Vai al contenuto</a>
'''

def header(active):
    links = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV if h != 'index.html')
    return f'''<header class="header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Euroceramiche — Home">{LOGO}</a>
    <nav class="nav" id="nav" aria-label="Principale">
      {links}
      <a class="btn" href="contatti.html#preventivo">Preventivo gratuito</a>
    </nav>
    <a class="btn" href="contatti.html#preventivo">Preventivo gratuito</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Apri il menu">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path class="l1" d="M3 8.5h18"/><path class="l2" d="M3 15.5h18"/></svg>
    </button>
  </div>
</header>
<main id="main">
'''

FOOTER = f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="index.html" aria-label="Euroceramiche — Home">{LOGO}</a>
        <div class="stars" aria-hidden="true">{ic('star')}{ic('star')}{ic('star')}</div>
        <p>Arredo bagno, pavimenti, rivestimenti, sanitari e rubinetteria. Showroom a Niscemi, al servizio di Niscemi, Gela e dintorni.</p>
      </div>
      <div>
        <h2>Prodotti</h2>
        <ul><li><a href="arredo-bagno.html">Arredo bagno</a></li><li><a href="pavimenti-rivestimenti.html">Pavimenti e rivestimenti</a></li><li><a href="sanitari-rubinetteria.html">Sanitari e rubinetteria</a></li></ul>
      </div>
      <div>
        <h2>Azienda</h2>
        <ul><li><a href="chi-siamo.html">Chi siamo</a></li><li><a href="servizi.html">Servizi</a></li><li><a href="contatti.html">Contatti</a></li><li><a href="contatti.html#preventivo">Preventivo gratuito</a></li></ul>
      </div>
      <div>
        <h2>Contatti</h2>
        <ul>
          <li><a href="contatti.html">Via Paolo VI, 23 · Niscemi (CL)</a></li>
          <li><a href="tel:+390933953210" data-tel="phone">+39 0933 953210</a></li>
          <li><a href="tel:+393203513244" data-tel="mobile">+39 320 351 3244</a></li>
          <li><a href="mailto:infoeuroceramiche@gmail.com" data-mail>infoeuroceramiche@gmail.com</a></li>
          <li><a href="https://www.instagram.com/euroceramicheniscemi/" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <span>© <span data-year>2026</span> Euroceramiche di Di Giovanni Donatella · Via Paolo VI, 23 — 93015 Niscemi (CL) · P.IVA 01619090853</span>
      <span><a href="privacy.html">Privacy</a> · Nessun cookie di profilazione · Foto: Pexels</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/393203513244" data-wa="Buongiorno, vorrei qualche informazione." target="_blank" rel="noopener" aria-label="Scrivici su WhatsApp">{ic('wa')}</a>
<nav class="mbar" aria-label="Azioni rapide">
  <a href="tel:+390933953210" data-tel="phone">{ic('phone')} Chiama</a>
  <a class="wa" href="https://wa.me/393203513244" data-wa="Buongiorno, vorrei qualche informazione." target="_blank" rel="noopener">{ic('wa')} WhatsApp</a>
  <a class="main" href="contatti.html#preventivo">Preventivo</a>
</nav>
<div class="toast" role="status" aria-live="polite"></div>
<script src="assets/js/site.js" defer></script>
</body>
</html>
'''

def quote_form(prefill=''):
    opts = ['Arredo bagno', 'Pavimenti', 'Rivestimenti', 'Sanitari e rubinetteria', 'Accessori', 'Progetto e rendering 3D', 'Ristrutturazione completa']
    options = ''.join(f'<option{" selected" if o == prefill else ""}>{o}</option>' for o in opts)
    amb = ''.join(f'<label class="choice"><input type="checkbox" name="ambienti" value="{a}"><span>{a}</span></label>' for a in ['Bagno', 'Cucina', 'Soggiorno', 'Camere', 'Esterni'])
    return f'''<section class="section section--dark" id="preventivo">
    <div class="wrap quote">
      <div class="quote-aside" data-reveal>
        {CUBE}
        <span class="eyebrow">Preventivo gratuito</span>
        <h2>Richiedi il tuo <strong>preventivo gratuito.</strong></h2>
        <p class="lead">Compila i campi principali: un nostro consulente ti ricontatta nel minor tempo possibile.</p>
        <ul>
          <li>{ic('check')} Gratuito e senza impegno</li>
          <li>{ic('check')} Progetto e rendering 3D per chi acquista</li>
          <li>{ic('check')} Consegna a domicilio inclusa nel prezzo</li>
        </ul>
      </div>
      <form class="form" data-quote-form novalidate data-reveal style="--i:1">
        <div class="form-row">
          <div class="field"><label for="q-nome">Nome e cognome</label><input id="q-nome" name="nome" autocomplete="name" required aria-describedby="e-nome"><span class="error" id="e-nome">Inserisci il tuo nome.</span></div>
          <div class="field"><label for="q-tel">Telefono</label><input id="q-tel" name="telefono" type="tel" inputmode="tel" autocomplete="tel" required aria-describedby="e-tel"><span class="error" id="e-tel">Inserisci un numero di telefono valido.</span></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="q-interesse">Mi interessa</label><select id="q-interesse" name="interesse">{options}</select></div>
          <div class="field"><label for="q-comune">Comune</label><input id="q-comune" name="comune" autocomplete="address-level2" placeholder="Es. Niscemi"></div>
        </div>
        <fieldset><legend class="legend">Ambienti</legend><div class="choices">{amb}</div></fieldset>
        <div class="field"><label for="q-mq">Metri quadri, se li conosci</label><input id="q-mq" name="mq" inputmode="decimal"></div>
        <div class="field"><label for="q-msg">Messaggio</label><textarea id="q-msg" name="messaggio" aria-describedby="h-msg"></textarea><span class="hint" id="h-msg">Stile, colori, tempi: tutto quello che ci aiuta a capire il progetto.</span></div>
        <div class="consent-wrap"><label class="consent"><input type="checkbox" name="privacy" required aria-describedby="e-priv"> <span>Ho letto l'<a href="privacy.html">informativa privacy</a> e acconsento a essere ricontattato.</span></label><span class="error" id="e-priv">Serve il consenso per poterti ricontattare.</span></div>
        <div class="submit">
          <button class="btn btn--wa" type="submit" value="whatsapp">{ic('wa')} Invia su WhatsApp</button>
          <button class="btn btn--line" type="submit" value="email">{ic('mail')} Invia via email</button>
          <small>Si apre WhatsApp o l'email con il messaggio già scritto: basta premere invia.</small>
        </div>
      </form>
    </div>
  </section>
'''

def page_head(crumb, title_html, lead, image=None, alt=''):
    pic = f'<div class="page-hero-img" data-reveal style="--i:2">{img(image, alt, 1600, 900, lazy=False)}</div>' if image else ''
    return f'''<section class="page-head">
    <div class="wrap">
      <nav class="crumbs" aria-label="Percorso"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">{crumb}</span></nav>
      <h1 data-reveal>{title_html}</h1>
      <p class="lead" data-reveal style="--i:1">{lead}</p>
      {pic}
    </div>
  </section>
'''

def cta_band(title_html, text, href='contatti.html#preventivo', label='Contattaci'):
    return f'''<section class="section section--dark">
    <div class="wrap band" data-reveal>
      {CUBE}
      <div><h2>{title_html}</h2><p class="lead" style="margin-top:14px">{text}</p></div>
      <a class="btn btn--light" href="{href}">{label} {ic('arrow')}</a>
    </div>
  </section>
'''

SERVICES = f'''<div class="services">
        <div class="service" data-reveal>{ic('truck')}<h3>Consegna a domicilio</h3><p>Già compresa nel prezzo finale: portiamo i materiali direttamente a casa vostra.</p></div>
        <div class="service" data-reveal style="--i:1">{ic('doc')}<h3>Preventivi gratuiti</h3><p>Chiari e senza impegno, per confrontare le soluzioni con calma.</p></div>
        <div class="service" data-reveal style="--i:2">{ic('render')}<h3>Progetto e rendering 3D</h3><p>Immagini fotorealistiche dei vostri ambienti, gratis per chi acquista.</p></div>
        <div class="service" data-reveal style="--i:3">{ic('chat')}<h3>Assistenza</h3><p>Un consulente vi segue prima, durante e dopo l'acquisto.</p></div>
      </div>'''

LOCAL_BUSINESS = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"HomeGoodsStore","name":"Euroceramiche","slogan":"Progettare insieme","telephone":"+39 0933 953210","email":"infoeuroceramiche@gmail.com","vatID":"IT01619090853","image":"assets/img/hero.webp",
"address":{"@type":"PostalAddress","streetAddress":"Via Paolo VI, 23","addressLocality":"Niscemi","postalCode":"93015","addressRegion":"CL","addressCountry":"IT"},
"areaServed":["Niscemi","Gela"],"sameAs":["https://www.instagram.com/euroceramicheniscemi/"],
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"13:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"15:00","closes":"20:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"15:00","closes":"19:00"}]}
</script>
'''

# ---------------------------------------------------------------- pagine
def home():
    slides = [
        ('hero.webp', 'Bagno con rivestimenti in marmo e vasca', 'Arredo bagno', 'Mobili, sanitari e rivestimenti coordinati'),
        ('living-marmo.webp', 'Soggiorno con parete rivestita in grandi lastre', 'Pavimenti e rivestimenti', 'Gres, parquet, pietre e decori'),
        ('nero-marquinia.webp', 'Lavabo su top in marmo nero con rubinetto', 'Sanitari e rubinetteria', 'Qualità che dura nel tempo'),
    ]
    sl = ''.join(f'<figure class="slide{" is-active" if k == 0 else ""}" aria-roledescription="diapositiva" aria-label="{k+1} di 3">{img(s, a, 1600, 1000, lazy=k > 0)}<figcaption><b>{t}</b>{c}</figcaption></figure>' for k, (s, a, t, c) in enumerate(slides))
    cats = [
        ('arredo-bagno.html', 'calacatta.webp', 'Bagno con vasca freestanding e mobile sospeso', 'Arredo bagno', 'Mobili, lavabi, specchiere, box doccia e vasche.'),
        ('pavimenti-rivestimenti.html', 'cemento.webp', 'Ambiente con pavimento in gres effetto legno', 'Pavimenti', 'Gres porcellanato, parquet e laminati.'),
        ('arredo-bagno.html#accessori', 'pietra-beige.webp', 'Bagno con nicchie, accessori e luci', 'Accessori', 'I dettagli che completano il bagno.'),
        ('pavimenti-rivestimenti.html#rivestimenti', 'pietra-lavica.webp', 'Parete rivestita in pietra scura', 'Rivestimenti', 'Decori, effetti materici e pietre.'),
        ('sanitari-rubinetteria.html', 'nero-marquinia.webp', 'Lavabo e rubinetto su top in marmo nero', 'Sanitari e rubinetteria', 'Vasi, bidet, miscelatori e colonne doccia.'),
        ('servizi.html', 'campioni.webp', 'Mani che confrontano campioni di materiali', 'Progetto 3D', 'Vedete il risultato prima di decidere.'),
    ]
    cg = ''.join(f'<a class="cat" href="{h}" data-reveal style="--i:{k % 3}"><div class="offset"><div class="frame">{img(s, a, 900, 600)}</div></div><h3>{t} {ic("arrow")}</h3><p>{d}</p></a>' for k, (h, s, a, t, d) in enumerate(cats))
    return (head('Euroceramiche Niscemi — Arredo bagno, pavimenti, rivestimenti e rubinetteria',
                 'Showroom Euroceramiche in Via Paolo VI a Niscemi: arredo bagno, pavimenti, rivestimenti, sanitari e rubinetteria. Preventivi e rendering 3D gratuiti, consegna a domicilio inclusa.', LOCAL_BUSINESS)
            + header('index.html') + f'''  <section class="hero" aria-label="Benvenuti">
    <div class="hero-text">
      <span class="eyebrow" data-reveal>{CUBE} Showroom a Niscemi</span>
      <h1 data-reveal style="--i:1">Il gusto di <strong>arredare,</strong> la cura di <strong>progettare insieme.</strong></h1>
      <p class="lead" data-reveal style="--i:2">Arredo bagno, pavimenti, rivestimenti, sanitari e rubinetteria dei marchi migliori. Vi aiutiamo a scegliere, progettiamo con voi e consegniamo a casa vostra.</p>
      <div class="hero-cta" data-reveal style="--i:3">
        <a class="btn" href="contatti.html#preventivo">Preventivo gratuito {ic('arrow')}</a>
        <a class="btn btn--line" href="#prodotti">Scopri i prodotti</a>
      </div>
      <div class="hero-meta" data-reveal style="--i:4">
        <span class="status" data-status><i></i><span>Orari showroom</span></span>
        <a href="contatti.html">Via Paolo VI, 23 · Niscemi</a>
        <a href="tel:+390933953210" data-tel="phone">0933 953210</a>
      </div>
    </div>
    <div class="slides" data-slider aria-roledescription="carosello" aria-label="Le nostre collezioni">
      {sl}
      <div class="slides-ui">
        <button type="button" data-slide-prev aria-label="Immagine precedente">{ic('prev')}</button>
        <span class="slides-count"><b data-slide-num>01</b> <span>/ 03</span></span>
        <button type="button" data-slide-next aria-label="Immagine successiva">{ic('next')}</button>
        <button type="button" data-slide-pause aria-label="Metti in pausa la presentazione">{ic('pause')}</button>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap intro">
      <div class="intro-text" data-reveal>
        <span class="eyebrow">Chi siamo</span>
        <h2>Da sempre al servizio <strong>dei nostri clienti.</strong></h2>
        <p>Euroceramiche è lo showroom di Niscemi per chi rinnova casa: pavimenti e rivestimenti, arredo bagno, sanitari, rubinetteria e accessori, scelti tra i produttori più affidabili.</p>
        <p>Ogni progetto parte da un ascolto attento: spazio, stile, abitudini e budget. Poi vi mostriamo le soluzioni, anche in 3D, finché non trovate quella giusta.</p>
        <a class="more" href="chi-siamo.html">Scopri chi siamo {ic('arrow')}</a>
      </div>
      <div class="offset" data-reveal style="--i:1"><div class="frame">{img('bagno-marmo.webp', 'Bagno con rivestimento in marmo e doccia in vetro', 1400, 934, srcset='assets/img/bagno-marmo-800.webp 800w, assets/img/bagno-marmo.webp 1400w', sizes='(max-width: 860px) 100vw, 50vw')}</div></div>
    </div>
  </section>

  <section class="section section--muted" id="prodotti">
    <div class="wrap">
      <div class="head" data-reveal>
        <span class="eyebrow">Prodotti</span>
        <h2>Tutto per la casa, <strong>in un solo showroom.</strong></h2>
        <p class="lead">Dall'arredo bagno ai pavimenti: collezioni da vedere e toccare dal vivo, con un consulente al vostro fianco.</p>
      </div>
      <div class="cats">{cg}</div>
    </div>
  </section>

''' + cta_band('Il bello di progettare <strong>insieme a te.</strong>', 'Raccontateci la vostra idea: insieme la trasformiamo in un progetto concreto, con immagini, misure e un preventivo chiaro.') + f'''
  <section class="section">
    <div class="wrap">
      <div class="head" data-reveal>
        <span class="eyebrow">Servizi</span>
        <h2>Vi seguiamo <strong>prima, durante e dopo.</strong></h2>
        <p class="lead">Professionalità, esperienza e passione per la ceramica, al servizio del vostro progetto.</p>
      </div>
      {SERVICES}
      <p style="margin-top:36px" data-reveal><a class="more" href="servizi.html">Tutti i servizi {ic('arrow')}</a></p>
    </div>
  </section>

  <section class="section section--muted" style="padding-top:clamp(64px,8vw,104px)">
    <div class="wrap">
      <div class="head" data-reveal>
        <span class="eyebrow">Partner</span>
        <h2>Alcuni dei <strong>nostri partner.</strong></h2>
        <p class="lead">Ci affidiamo ai produttori migliori per arredo bagno, ceramiche e rubinetteria.</p>
      </div>
      <div data-reveal>{brands(['Imola', 'Dado Ceramica', 'Herberia', 'FAP', 'Faetano', 'Flab', 'Gattoni', 'Vica'])}</div>
    </div>
  </section>

''' + quote_form() + FOOTER)

def chi_siamo():
    return (head('Chi siamo — Euroceramiche Niscemi', 'Euroceramiche: showroom di arredo bagno, pavimenti, rivestimenti, sanitari e rubinetteria a Niscemi. Professionalità, esperienza e passione per la ceramica.')
            + header('chi-siamo.html')
            + page_head('Chi siamo', 'Professionalità, esperienza e <strong>passione per la ceramica.</strong>',
                        'Uno showroom a Niscemi dove scegliere con calma e con qualcuno che conosce davvero i materiali.',
                        'living-marmo.webp', 'Soggiorno con parete in grandi lastre effetto marmo')
            + f'''  <section class="section">
    <div class="wrap">
      <div class="split">
        <div class="prose" data-reveal>
          <span class="eyebrow">La nostra storia</span>
          <h2>Un punto di riferimento <strong>per la casa.</strong></h2>
          <p>Euroceramiche è specializzata in pavimenti e rivestimenti, arredo bagno, sanitari, rubinetteria e accessori. Nel tempo ci siamo guadagnati la fiducia di tante famiglie di Niscemi, Gela e dintorni grazie a materiali di prima scelta e a un servizio attento.</p>
          <p>Lavoriamo con produttori affermati e seguiamo le novità del settore, per proporre soluzioni belle da vedere e fatte per durare.</p>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('calacatta.webp', 'Bagno con vasca freestanding e rivestimenti chiari', 900, 632)}</div></div>
      </div>
      <div class="split split--rev">
        <div class="prose" data-reveal>
          <span class="eyebrow">Come lavoriamo</span>
          <h2>Ascoltare, proporre, <strong>mostrare.</strong></h2>
          <ul class="list">
            <li>Partiamo dal vostro spazio e dalle vostre abitudini, non dal catalogo.</li>
            <li>Vi proponiamo poche soluzioni, ben ragionate, tra i marchi che trattiamo.</li>
            <li>Vi mostriamo il risultato con un rendering 3D prima di decidere.</li>
            <li>Consegniamo a domicilio e restiamo disponibili anche dopo.</li>
          </ul>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('campioni.webp', 'Mani che confrontano campioni di marmo', 1400, 934, srcset='assets/img/campioni-800.webp 800w, assets/img/campioni.webp 1400w', sizes='(max-width: 860px) 100vw, 50vw')}</div></div>
      </div>
    </div>
  </section>
''' + cta_band('Venite a <strong>trovarci.</strong>', 'Lo showroom è in Via Paolo VI, 23 a Niscemi, aperto dal lunedì al sabato.', 'contatti.html', 'Orari e contatti') + quote_form() + FOOTER)

def arredo_bagno():
    return (head('Arredo bagno a Niscemi e Gela — Euroceramiche', 'Arredo bagno a Niscemi: mobili, lavabi, specchiere, box doccia, vasche, idromassaggio e accessori. Palombini, Royo, Blue Life, Vica, Eban e altri marchi.')
            + header('arredo-bagno.html')
            + page_head('Arredo bagno', 'Arredare il bagno <strong>con stile.</strong>',
                        'Mobili, sanitari, docce e accessori dei marchi più apprezzati, scelti insieme a un consulente e pensati per il vostro spazio.',
                        'hero.webp', 'Bagno elegante con rivestimenti in marmo e vasca')
            + f'''  <section class="section">
    <div class="wrap">
      <div class="split">
        <div class="prose" data-reveal>
          <span class="eyebrow">La collezione bagno</span>
          <h2>Bello, pratico, <strong>su misura.</strong></h2>
          <p>Nel nostro showroom trovate l'assortimento completo per il bagno. Teniamo conto di tutto: spazio disponibile, stile della casa, abitudini di chi lo usa, integrazione tra vecchio e nuovo.</p>
          <ul class="list">
            <li>Mobili lavabo e lavabi</li>
            <li>Specchiere, anche con illuminazione integrata</li>
            <li>Box doccia: cabine, piatti doccia e vetri su misura</li>
            <li>Vasche da bagno e idromassaggio</li>
            <li>Termoarredo e termoidraulica</li>
          </ul>
          <a class="btn" href="#preventivo" data-quote="Arredo bagno">Preventivo per il bagno {ic('arrow')}</a>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('calacatta.webp', 'Bagno con vasca freestanding e mobile sospeso', 900, 632)}</div></div>
      </div>
      <div class="split split--rev" id="accessori">
        <div class="prose" data-reveal>
          <span class="eyebrow">Accessori</span>
          <h2>I dettagli che <strong>fanno la differenza.</strong></h2>
          <p>Portasciugamani, mensole, specchi, luci e complementi coordinati con finiture e rubinetteria, per un bagno curato in ogni parte.</p>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('pietra-beige.webp', 'Bagno con nicchie, accessori e luci', 900, 601)}</div></div>
      </div>
    </div>
  </section>

  <section class="section section--muted">
    <div class="wrap">
      <div class="head" data-reveal><span class="eyebrow">Marchi</span><h2>I marchi <strong>per il bagno.</strong></h2></div>
      <div data-reveal>{brands(BRANDS_BAGNO)}</div>
    </div>
  </section>
''' + quote_form('Arredo bagno') + FOOTER)

def pavimenti():
    return (head('Pavimenti e rivestimenti a Niscemi e Gela — Euroceramiche', 'Pavimenti e rivestimenti a Niscemi: gres porcellanato, parquet e laminati, pietre naturali e ricostruite, ceramiche decorative. Imola, Dado Ceramica, Herberia, FAP.')
            + header('pavimenti-rivestimenti.html')
            + page_head('Pavimenti e rivestimenti', 'Superfici per ogni <strong>ambiente.</strong>',
                        'Gres porcellanato, parquet e laminati, pietre naturali e ricostruite: per interni ed esterni, in ogni formato e finitura.',
                        'legno.webp', 'Soggiorno con pavimento in legno posato a spina di pesce')
            + f'''  <section class="section">
    <div class="wrap">
      <div class="split">
        <div class="prose" data-reveal>
          <span class="eyebrow">Pavimenti</span>
          <h2>Gres <strong>porcellanato.</strong></h2>
          <p>Resistente, impermeabile e facile da pulire: si adatta a qualunque stile. Disponibile smaltato, lappato o levigato, per la casa e per gli spazi professionali.</p>
          <a class="btn" href="#preventivo" data-quote="Pavimenti">Preventivo pavimenti {ic('arrow')}</a>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('cemento.webp', 'Ambiente con pavimento in gres e parete effetto cemento', 900, 601)}</div></div>
      </div>
      <div class="split split--rev">
        <div class="prose" data-reveal>
          <span class="eyebrow">Pavimenti</span>
          <h2>Parquet <strong>e laminati.</strong></h2>
          <p>Il legno dà calore e carattere a ogni ambiente. Proponiamo pavimenti in legno massello tradizionale e prefiniti multistrato, con uno strato superiore in legno nobile di spessore variabile.</p>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('legno-900.webp', 'Pavimento in legno a spina di pesce', 900, 601)}</div></div>
      </div>
      <div class="split" id="rivestimenti">
        <div class="prose" data-reveal>
          <span class="eyebrow">Rivestimenti</span>
          <h2>Pareti con <strong>personalità.</strong></h2>
          <p>Ceramiche decorative, effetti materici, pietre naturali e ricostruite per bagni, cucine e pareti d'arredo, in tanti formati, colori e stili.</p>
          <a class="btn" href="#preventivo" data-quote="Rivestimenti">Preventivo rivestimenti {ic('arrow')}</a>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('pietra-lavica.webp', 'Parete rivestita in pietra scura con mensola', 900, 900)}</div></div>
      </div>
    </div>
  </section>

  <section class="section section--muted">
    <div class="wrap">
      <div class="head" data-reveal><span class="eyebrow">Marchi</span><h2>Ceramiche <strong>e superfici.</strong></h2></div>
      <div data-reveal>{brands(BRANDS_CER)}</div>
    </div>
  </section>
''' + quote_form('Pavimenti') + FOOTER)

def sanitari():
    return (head('Sanitari e rubinetteria a Niscemi e Gela — Euroceramiche', 'Sanitari e rubinetteria a Niscemi: vasi, bidet, lavabi, miscelatori e colonne doccia. Carlo Frattini, Mamoli, Morini, Keller Taps, Gattoni, Paffoni e altri.')
            + header('sanitari-rubinetteria.html')
            + page_head('Sanitari e rubinetteria', 'Rubinetteria <strong>di qualità.</strong>',
                        'Sanitari e rubinetteria scelti per durare, funzionare bene ogni giorno e ridurre lo spreco d’acqua.',
                        'bagno.webp', 'Bagno con lavabo, specchio illuminato e rubinetteria')
            + f'''  <section class="section">
    <div class="wrap">
      <div class="split">
        <div class="prose" data-reveal>
          <span class="eyebrow">Rubinetteria</span>
          <h2>Bella da vedere, <strong>fatta per durare.</strong></h2>
          <p>Scegliere bene la rubinetteria conta: incide sull'aspetto del bagno, sulla comodità di tutti i giorni e sui consumi. Per questo proponiamo solo prodotti realizzati con materiali e tecnologie affidabili.</p>
          <ul class="list">
            <li>Miscelatori per lavabo, bidet e vasca</li>
            <li>Colonne e soffioni doccia</li>
            <li>Sistemi che riducono il consumo d'acqua</li>
          </ul>
          <a class="btn" href="#preventivo" data-quote="Sanitari e rubinetteria">Chiedi un preventivo {ic('arrow')}</a>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('nero-marquinia.webp', 'Lavabo d’appoggio e rubinetto su top in marmo nero', 900, 601)}</div></div>
      </div>
      <div class="split split--rev">
        <div class="prose" data-reveal>
          <span class="eyebrow">Sanitari</span>
          <h2>Comfort <strong>e pulizia.</strong></h2>
          <p>Vasi, bidet e lavabi in ceramica di qualità, sospesi o a terra, coordinati con mobili e accessori. Vi aiutiamo a scegliere forme e dimensioni giuste per il vostro bagno.</p>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('pietra-beige.webp', 'Bagno con sanitari sospesi e mobile lavabo', 900, 601)}</div></div>
      </div>
    </div>
  </section>

  <section class="section section--muted">
    <div class="wrap">
      <div class="head" data-reveal><span class="eyebrow">Marchi</span><h2>Sanitari <strong>e rubinetteria.</strong></h2></div>
      <div data-reveal>{brands(BRANDS_RUB)}</div>
    </div>
  </section>
''' + quote_form('Sanitari e rubinetteria') + FOOTER)

def servizi():
    return (head('Servizi — Rendering 3D, preventivi gratuiti e consegna — Euroceramiche Niscemi', 'Progettazione e rendering 3D gratuiti, preventivi gratuiti, consegna a domicilio inclusa, assistenza pre e post vendita. Showroom Euroceramiche a Niscemi.')
            + header('servizi.html')
            + page_head('Servizi', 'Vi aiutiamo a realizzare <strong>la casa che avete in mente.</strong>',
                        'Progettazione, rendering 3D e preventivi gratuiti, consegna inclusa e assistenza prima e dopo la vendita.',
                        'campioni.webp', 'Mani che confrontano campioni di materiali su un tavolo di progetto')
            + f'''  <section class="section">
    <div class="wrap">
      {SERVICES}
    </div>
  </section>

  <section class="section section--muted">
    <div class="wrap">
      <div class="split">
        <div class="prose" data-reveal>
          <span class="eyebrow">Progettazione e rendering 3D</span>
          <h2>Niente lasciato <strong>all'immaginazione.</strong></h2>
          <p>Piantine e disegni spesso non bastano per capire come sarà davvero un ambiente. Partendo dalle vostre misure creiamo modelli tridimensionali e immagini fotorealistiche: spazi, volumi, arredi e finiture, come se ci foste dentro.</p>
          <ul class="list">
            <li>Gratuito per chi acquista i materiali da noi</li>
            <li>Basato sulle misure reali dei vostri ambienti</li>
            <li>Per chi lo desidera, collaborazione con un team di architetti</li>
          </ul>
          <a class="btn" href="#preventivo" data-quote="Progetto e rendering 3D">Richiedi il tuo progetto {ic('arrow')}</a>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('living-marmo-900.webp', 'Soggiorno progettato con parete in lastre e mensole in legno', 900, 600)}</div></div>
      </div>
      <div class="split split--rev">
        <div class="prose" data-reveal>
          <span class="eyebrow">Pre e post vendita</span>
          <h2>Un consulente <strong>tutto per voi.</strong></h2>
          <p>Vi accogliamo in showroom e, se volete, fissiamo un appuntamento per dedicare al vostro progetto tutto il tempo che serve. E dopo l'acquisto restiamo a disposizione: sapete sempre a chi rivolgervi.</p>
        </div>
        <div class="offset" data-reveal style="--i:1"><div class="frame">{img('cucina-900.webp', 'Cucina luminosa con isola e pavimento chiaro', 900, 603)}</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="head" data-reveal><span class="eyebrow">Domande frequenti</span><h2>Prima di <strong>chiedere.</strong></h2></div>
      <div class="faq" data-reveal>
        <details><summary>Il preventivo è davvero gratuito?</summary><p>Sì, gratuito e senza impegno. Potete chiederlo in showroom, per telefono o da questo sito.</p></details>
        <details><summary>Quanto costa il rendering 3D?</summary><p>Nulla per chi acquista i materiali da noi: progetto, rendering e preventivo sono compresi.</p></details>
        <details><summary>La consegna si paga a parte?</summary><p>No: la consegna a domicilio è già compresa nel prezzo finale.</p></details>
        <details><summary>Serve un appuntamento?</summary><p>No, siete i benvenuti negli orari di apertura. Per un progetto completo però conviene prenotare, così avrete più tempo dedicato.</p></details>
      </div>
    </div>
  </section>
''' + quote_form('Progetto e rendering 3D') + FOOTER)

def contatti():
    days = [(1, 'Lunedì', '08:00-13:00,15:00-20:00', '8:00–13:00 · 15:00–20:00'), (2, 'Martedì', '08:00-13:00,15:00-20:00', '8:00–13:00 · 15:00–20:00'),
            (3, 'Mercoledì', '08:00-13:00,15:00-20:00', '8:00–13:00 · 15:00–20:00'), (4, 'Giovedì', '08:00-13:00,15:00-20:00', '8:00–13:00 · 15:00–20:00'),
            (5, 'Venerdì', '08:00-13:00,15:00-20:00', '8:00–13:00 · 15:00–20:00'), (6, 'Sabato', '08:00-13:00,15:00-19:00', '8:00–13:00 · 15:00–19:00'), (0, 'Domenica', '', 'Chiuso')]
    rows = ''.join(f'<tr data-day="{d}" data-hours="{h}"><th scope="row">{n}</th><td>{t}</td></tr>' for d, n, h, t in days)
    return (head('Contatti e orari — Euroceramiche, Via Paolo VI 23, Niscemi', 'Euroceramiche, Via Paolo VI 23, 93015 Niscemi (CL). Tel. 0933 953210, cell. 320 3513244, infoeuroceramiche@gmail.com. Orari e preventivo gratuito.', LOCAL_BUSINESS)
            + header('contatti.html')
            + page_head('Contatti', 'Siamo felici <strong>di aiutarvi.</strong>',
                        'Venite in showroom, chiamateci o scriveteci: più dettagli ci date sul progetto, più precisa sarà la nostra risposta.')
            + f'''  <section class="section">
    <div class="wrap contact">
      <div class="info" data-reveal>
        <span class="status" data-status><i></i><span>Orari showroom</span></span>
        <address><strong>Euroceramiche</strong><br>Via Paolo VI, 23<br>93015 Niscemi (CL)</address>
        <div class="channels">
          <a href="tel:+390933953210" data-tel="phone">{ic('phone')} +39 0933 953210</a>
          <a href="tel:+393203513244" data-tel="mobile">{ic('phone')} +39 320 351 3244</a>
          <a href="https://wa.me/393203513244" data-wa="Buongiorno, vorrei qualche informazione." target="_blank" rel="noopener">{ic('wa')} Scrivici su WhatsApp</a>
          <a href="mailto:infoeuroceramiche@gmail.com" data-mail>{ic('mail')} infoeuroceramiche@gmail.com</a>
          <a href="https://www.instagram.com/euroceramicheniscemi/" target="_blank" rel="noopener">{ic('ig')} @euroceramicheniscemi</a>
        </div>
      </div>
      <div class="map-card" data-reveal style="--i:1">
        <h2 style="font-size:1.5rem;font-weight:600">Orari di apertura</h2>
        <!-- Orari: unica fonte di verità per lo stato "aperto ora". Formato: HH:MM-HH:MM separati da virgola. -->
        <table class="hours" aria-label="Orari di apertura">{rows}</table>
        <a class="btn" href="https://www.google.com/maps/dir/?api=1&destination=Euroceramiche%2C+Via+Paolo+VI+23%2C+93015+Niscemi+CL" data-maps target="_blank" rel="noopener">{ic('pin')} Indicazioni stradali</a>
      </div>
    </div>
  </section>
''' + quote_form() + FOOTER)

def privacy():
    return (head('Privacy e cookie — Euroceramiche', 'Informativa privacy e cookie di Euroceramiche, Niscemi.')
            + header('')
            + page_head('Privacy e cookie', 'Informativa <strong>privacy.</strong>', 'Modello da far verificare a un consulente prima della pubblicazione.')
            + '''  <section class="section">
    <div class="wrap prose" style="max-width:760px">
      <h2 style="font-size:1.6rem;font-weight:600">Titolare del trattamento</h2>
      <p>Euroceramiche di Di Giovanni Donatella, Via Paolo VI, 23 — 93015 Niscemi (CL), P.IVA 01619090853. Email: infoeuroceramiche@gmail.com · Tel. +39 0933 953210.</p>
      <h2 style="font-size:1.6rem;font-weight:600">Quali dati e perché</h2>
      <p>Solo i dati che ci inviate voi tramite il modulo, WhatsApp, telefono o email (nome, telefono, comune, informazioni sul progetto), usati esclusivamente per rispondere alla richiesta e preparare il preventivo (art. 6.1.b GDPR).</p>
      <h2 style="font-size:1.6rem;font-weight:600">Come vengono trasmessi</h2>
      <p>Il modulo non salva dati sul sito: apre WhatsApp o il vostro programma di posta con il messaggio già scritto, che decidete voi se inviare. WhatsApp è un servizio di WhatsApp Ireland Ltd., con una propria informativa.</p>
      <h2 style="font-size:1.6rem;font-weight:600">Cookie</h2>
      <p>Il sito non usa cookie di profilazione né servizi di terze parti: caratteri e immagini sono ospitati sul sito stesso. Per questo non serve un banner cookie.</p>
      <h2 style="font-size:1.6rem;font-weight:600">I vostri diritti</h2>
      <p>Potete chiedere accesso, rettifica o cancellazione dei dati scrivendo a infoeuroceramiche@gmail.com, e proporre reclamo al Garante per la protezione dei dati personali.</p>
    </div>
  </section>
''' + FOOTER)

PAGES = {'index.html': home, 'chi-siamo.html': chi_siamo, 'arredo-bagno.html': arredo_bagno,
         'pavimenti-rivestimenti.html': pavimenti, 'sanitari-rubinetteria.html': sanitari,
         'servizi.html': servizi, 'contatti.html': contatti, 'privacy.html': privacy}

if __name__ == '__main__':
    for name, fn in PAGES.items():
        (ROOT / name).write_text(fn(), encoding='utf-8')
        print('scritto', name)
