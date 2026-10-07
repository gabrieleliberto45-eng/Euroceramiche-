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

- **Fotografia prima di tutto**: hero a tutto schermo, ambienti e dettagli di
  materia. Le foto attuali sono stock Pexels (licenza gratuita anche commerciale)
  e vanno sostituite con quelle dello showroom e delle collezioni reali.
- **Palette**: carta calda (sfondo), inchiostro quasi nero, sezioni scure per il
  ritmo, oro tenue in dettagli minimi. Il cobalto solo per il focus.
- **Tipografia**: *Bodoni Moda* regular per i titoli, grandi e con corsivo come
  accento; *Hanken Grotesk* per il testo; etichette in maiuscoletto spaziato
  con numerazione di sezione (01, 02…). Font self-hosted.
- **Layout**: molto bianco, griglia a 12 colonne, collage asimmetrici, angoli
  quasi vivi, linee sottili al posto dei riquadri. Niente card arrotondate,
  niente statistiche inventate.

## Principi di interazione (motion)

- Lento e misurato: rivelazioni a sipario delle foto (clip-path + leggero
  zoom che si assesta), titoli che salgono parola per parola, testo del
  manifesto che si "accende" leggendo, parallasse leggera.
- Un solo momento scenografico: la galleria "Ambienti" orizzontale bloccata
  durante lo scroll (su mobile diventa uno scorrimento a scatto).
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

## Dati da completare prima della pubblicazione

Tutti i segnaposto sono tra parentesi quadre `[ ]` nell'HTML e raccolti nel
blocco `CONFIG` in fondo a `index.html`:

- Numero WhatsApp Business e telefono fisso
- Indirizzo esatto, email, Partita IVA
- Orari reali dello showroom
- Nomi reali delle collezioni/marchi trattati
- Foto reali dello showroom e delle collezioni (cartella `img/`, stessi nomi file)
