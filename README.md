# Euroceramiche Niscemi — sito web

Sito a pagina singola, statico, senza dipendenze né build. Brief di brand e principi di design in [`PRODUCT.md`](PRODUCT.md).

## Struttura

```
index.html      pagina principale (CSS e JS inline)
privacy.html    informativa privacy (modello da completare)
fonts/          Bodoni Moda + Hanken Grotesk, self-hosted (licenza SIL OFL)
img/            foto WebP (provvisorie, da Pexels: vedi sotto)
```

## Prima di pubblicare

1. In fondo a `index.html`, compilare il blocco **`CONFIG`**: numero WhatsApp Business (formato `39XXXXXXXXXX`), telefono, email, indirizzo, P.IVA. Tutti i link e i testi di contatto si aggiornano da lì.
2. **Orari**: modificare le righe della tabella orari in `index.html` (`data-hours="08:30-13:00,15:30-19:30"`). Lo stato "Aperto ora / Chiuso" viene calcolato da quei valori, sull'ora italiana.
3. Aggiornare indirizzo e orari anche nel blocco **JSON-LD** in `<head>` (serve a Google).
4. **Collezioni**: sostituire i nomi d'esempio con le collezioni reali; ogni prodotto ha `data-cat` per i filtri (`marmo`, `legno`, `pietra`, `rivestimenti`, `esterni`).
5. **Foto**: le immagini in `img/` sono foto stock di [Pexels](https://www.pexels.com/license/) (uso commerciale gratuito, nessuna attribuzione obbligatoria). Sostituirle con foto reali mantenendo gli stessi nomi file (WebP, ~1600 px di lato lungo, versioni `-800`/`-900` per mobile). La foto accanto agli orari va sostituita con una dello showroom vero.
6. Completare `privacy.html` e farla verificare.

## Ricevere i preventivi

Il modulo apre WhatsApp o l'email con il messaggio già compilato: non serve un server. Per salvare anche le richieste online, creare un modulo su Formspree o Netlify Forms e inserirne l'URL in `CONFIG.formEndpoint`.

## Pubblicazione

Qualsiasi hosting statico: GitHub Pages, Netlify, Cloudflare Pages o il proprio spazio web (caricare la cartella così com'è).
