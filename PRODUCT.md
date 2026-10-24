# PRODUCT.md — Euroceramiche Niscemi

Documento di riferimento per chi lavora sul sito (persone o agenti AI).
Ogni scelta di design e di testo deve poter essere ricondotta a questo file.

## Chi siamo

Rivenditore di ceramiche, piastrelle e arredo bagno di alta qualità a
**Niscemi (CL), Sicilia**. Showroom fisico con ambienti allestiti e campionario
completo. A 15 km da Caltagirone, capitale della maiolica siciliana: la
tradizione ceramica è parte dell'identità del territorio.

## Per chi è il sito

| Pubblico | Cosa cerca | Cosa deve trovare in 10 secondi |
|---|---|---|
| **Privati** che ristrutturano casa o bagno | Ispirazione, rassicurazione, un prezzo indicativo | Collezioni, "come lavoriamo", preventivo gratuito, WhatsApp |
| **Professionisti** (posatori, imprese, architetti, geometri) | Disponibilità, tempi, condizioni dedicate | Listino riservato, consegna in cantiere, campionature, contatto diretto |

Gran parte del traffico arriva **da smartphone**, spesso da Google Maps o da un
link WhatsApp. Il sito è una pagina sola, deve caricare in fretta anche su 4G
e portare a un'azione: **chiedere un preventivo, scrivere su WhatsApp,
venire in showroom**.

## Obiettivi (in ordine)

1. Richieste di preventivo (form → WhatsApp o email)
2. Conversazioni WhatsApp Business
3. Visite in showroom (indirizzo, orari, stato "aperto ora", indicazioni)
4. Fiducia: competenza, materiali veri, persone reali del territorio

## Personalità del brand

**Lusso editoriale, sobrio e serio.** Il tono dei grandi marchi italiani della
ceramica: poche parole, fotografia protagonista, nessun effetto "giocattolo".
Parliamo come un consulente esperto: diretto, cordiale, senza superlativi vuoti.

- Sì: "Portiamo i campioni a casa vostra." "Vi rispondiamo in giornata."
- No: "Soluzioni innovative all'avanguardia per ogni esigenza."

Il registro è il **voi** di cortesia per i testi generali, il **tu** solo nei
pulsanti brevi ("Scrivici su WhatsApp").

## Direzione visiva

**Scuro cinematografico** (dal 8/10/2026; la versione chiara precedente è in
`versione-chiara.html`).

- **Fotografia protagonista** a tutto schermo, su fondo nero caldo.
- **Palette**: nero caldo, superfici antracite, testo avorio, grigio per la
  seconda metà dei titoli, **ambra** come unico accento (pulsanti, voce attiva,
  indicatori). Mai bianco puro come sfondo.
- **Tipografia**: *Hanken Grotesk* per tutto; titoli in semibold con spaziatura
  stretta, etichette in maiuscolo spaziato con numerazione "01 / 04".
- **Elementi**: navigazione a pillola di vetro al centro con voce attiva ambra,
  pulsanti ambra a pillola, tag a pillola sottili, foto con angoli morbidi e
  alcune ad arco, sezioni come pannelli arrotondati.

## Principi di interazione (motion)

- Lento e misurato: rivelazioni a sipario delle foto (clip-path + leggero
  zoom che si assesta), titoli che salgono parola per parola, testo del
  manifesto che si "accende" leggendo, parallasse leggera.
- Apertura cinematografica: "viaggio" di 4 scene bloccato durante lo scroll; la
  foto fa zoom in avanti, si scurisce, e la scena successiva entra da una
  "porta" che si apre fino a tutto schermo; indicatore di avanzamento laterale. Solo transform e clip-path: fluido anche su iPhone.
- Galleria "Ambienti" orizzontale bloccata durante lo scroll (su mobile diventa
  uno scorrimento a scatto).
- Header trasparente sulla foto, solido dopo; si nasconde scendendo e riappare
  salendo.
- Hover solo su dispositivi con puntatore fine; feedback alla pressione discreto.
- `prefers-reduced-motion` rispettato ovunque.

## Vincoli tecnici

- Un solo `index.html` con CSS e JS inline, nessuna dipendenza, nessun build.
- HTML < 30 KB compressi; foto in WebP con `srcset` e caricamento lazy (~850 KB totali, scaricate solo quando servono); nessun cookie di terze parti
  → nessun banner cookie necessario.
- Accessibilità: contrasto AA, focus visibile, target touch ≥ 44 px,
  form con etichette ed errori leggibili dagli screen reader.
- SEO locale: dati strutturati `HomeGoodsStore`, titolo e description con
  "Niscemi", orari e indirizzo in chiaro.

## Dati reali (fonte: sito attuale euroceramiche-niscemi.it, ottobre 2026)

- **Ragione sociale**: Euroceramiche di Di Giovanni Donatella · P.IVA 01619090853
- **Indirizzo**: Via Paolo VI, 23 — 93015 Niscemi (CL)
  (la pagina "Servizi" del vecchio sito indica lo showroom al n. 27: da verificare)
- **Telefono**: +39 0933 953210 · **Cellulare/WhatsApp**: +39 320 351 3244
- **Email**: infoeuroceramiche@gmail.com · **Instagram**: @euroceramicheniscemi
- **Orari** (da directory online, da verificare): lun–ven 8–13 / 15–20, sab 8–13 / 15–19
- **Servizi**: progettazione e rendering 3D gratuiti per chi acquista, preventivi
  gratuiti, consegna a domicilio inclusa nel prezzo, assistenza pre e post vendita,
  collaborazione con un team di architetti, appuntamenti dedicati
- **Categorie**: arredo bagno, sanitari e rubinetteria, accessori e illuminazione,
  gres porcellanato, parquet e laminati, rivestimenti e pietre
- **Marchi (23)**: Palombini, Royo, Blue Life, Vica, Eban, Legno Bagno, Global Trade,
  Progetto Idea Stella, Carlo Frattini, Mamoli, Morini, Keller Taps, Gattoni,
  Paffoni, CSA, New Flag, Azzurra, Dado Ceramica, Imola, Herberia, FAP, Faetano, Flab
- **Marchio**: cubo in linea + "EUROCERAMICHE", motto "progettare insieme"

I testi del sito sono riscritti da zero: dal vecchio sito sono presi solo i dati.

## Ancora da fare prima della pubblicazione

- Foto reali dello showroom e dei lavori (le attuali sono stock Pexels)
- Verificare orari e numero civico, e che il 320 351 3244 sia su WhatsApp Business
