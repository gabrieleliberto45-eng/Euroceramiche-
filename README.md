# Euroceramiche Niscemi — sito web

Nuova versione del sito **euroceramiche-niscemi.it**: stessa struttura e stessa identità
(bianco e nero, logo a cubo, motto "progettare insieme"), migliorata con la skill
**UI/UX Pro Max** (`.claude/skills/ui-ux-pro-max`). Testi riscritti da zero; dal vecchio
sito sono presi solo i dati (contatti, servizi, categorie, marchi).

## Struttura

```
index.html                    Home
chi-siamo.html                Chi siamo
arredo-bagno.html             Arredo bagno (+ accessori)
pavimenti-rivestimenti.html   Pavimenti e rivestimenti
sanitari-rubinetteria.html    Sanitari e rubinetteria
servizi.html                  Servizi, rendering 3D, FAQ
contatti.html                 Contatti, orari, indicazioni
privacy.html                  Informativa privacy (da far verificare)
assets/css/site.css           stile comune
assets/js/site.js             script comune + CONFIG (contatti, WhatsApp)
assets/img, assets/fonts      foto (stock Pexels, provvisorie) e carattere self-hosted
tools/build.py                genera tutte le pagine (header, footer e modulo condivisi)
design-system/euroceramiche/  sistema di design della skill + decisioni applicate
archivio/                     versioni precedenti (scura cinematografica, chiara)
```

## Modificare il sito

- Testi e pagine: modificare `tools/build.py`, poi `python3 tools/build.py`.
- Contatti e numero WhatsApp: blocco `CONFIG` in `assets/js/site.js`.
- Orari: tabella in `contatti()` dentro `tools/build.py` (formato `HH:MM-HH:MM`).
- Foto: sostituire i file in `assets/img/` mantenendo gli stessi nomi.

## Prima di pubblicare

- Foto reali dello showroom e dei lavori.
- Verificare orari, numero civico (23 o 27) e numero WhatsApp.
- Far verificare `privacy.html`.

Pubblicazione: qualsiasi hosting statico (GitHub Pages, Netlify, spazio web) — si carica la cartella così com'è.
