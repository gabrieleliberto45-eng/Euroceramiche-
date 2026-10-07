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

**Concreta, artigiana, mediterranea.** Non lusso ostentato: qualità che si
tocca con mano. Parliamo come un consulente esperto dietro il bancone dello
showroom: diretto, cordiale, senza superlativi vuoti.

- Sì: "Portiamo i campioni a casa vostra." "Vi rispondiamo in giornata."
- No: "Soluzioni innovative all'avanguardia per ogni esigenza."

Il registro è il **voi** di cortesia per i testi generali, il **tu** solo nei
pulsanti brevi ("Scrivici su WhatsApp").

## Direzione visiva

- **Palette**: pietra calcarea chiara (sfondo), inchiostro blu-nero (testo),
  **blu cobalto della maiolica** come unico colore d'accento, ocra solo in
  dettagli minimi. Niente gradienti viola, niente neon, niente nero/grigio puri.
- **Tipografia**: *Bodoni Moda* per i titoli (Bodoni è il carattere italiano per
  eccellenza, contrasto alto come una superficie lucidata), *Hanken Grotesk*
  per il testo. Font self-hosted, niente richieste a terzi.
- **Materia prima ai prodotti**: le anteprime delle collezioni sono texture
  generate (marmo, legno, cemento, cotto, maiolica) con le fughe in scala reale
  sul formato della piastrella. Il sito è bello anche senza foto e resta leggero;
  quando arrivano le foto vere si sostituiscono.
- **Layout**: asimmetrico, molto respiro, griglie a fuga come un pavimento posato.
  Niente card dentro card, niente "numeroni" di statistiche inventate.

## Principi di interazione (motion)

- Easing **ease-out** personalizzati, durate 150–300 ms: l'interfaccia deve
  sembrare istantanea. Nessun bounce.
- Feedback alla pressione: `scale(.97)` sui pulsanti.
- Hover solo su dispositivi con puntatore fine (`hover: hover`).
- Popover e menu nascono dal punto d'origine (`transform-origin`), mai da `scale(0)`.
- Transizioni interrompibili (CSS transitions, non keyframe) per ciò che
  l'utente può invertire.
- Filtro collezioni con View Transitions dove supportate.
- Effetti "wow" su base chiara: intro col logo che si compone, parete 3D di
  campioni che si assemblano in volo su un pavimento di marmo, pulsanti magnetici,
  piastrelle che si posano entrando nello schermo. Hero con pavimento 3D e luce
  che segue il cursore, sezione materiali bloccata allo scroll con lastra 3D,
  titoli rivelati parola per parola, schede con inclinazione 3D.
- `prefers-reduced-motion` rispettato ovunque.

## Vincoli tecnici

- Un solo `index.html` con CSS e JS inline, nessuna dipendenza, nessun build.
- Peso pagina (senza foto) < 150 KB compressi; nessun cookie di terze parti
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
- Nomi reali delle collezioni/marchi trattati e foto (cartella `img/`)
