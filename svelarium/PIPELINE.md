# Svelarium: produzione giornaliera automatica

Canale: **Svelarium** ("ogni giorno un segreto svelato"). Lingua: italiano.
Ogni giorno: **3 Short** (uno di **storia**, uno di **misteri**, uno di **scienza**) per il **giorno dopo**,
consegnati all'utente come file + testi: li carica lui a mano su YouTube Shorts e TikTok (niente Metricool).

## Risorse fisse
- Metricool brand Svelarium (`blogId 8287937`) NON si usa più per pubblicare. MAI usare il brand `riskly63`.
- Higgsfield (piano PLUS): immagini `gpt_image_2_6`, `aspect_ratio 9:16`; voce `text2speech_v2`,
  `variant elevenlabs`, `voice_type preset`, `voice_id 95429266-c0ac-4137-a209-63b8812b0f23`, `use_unlim false`.
- Max 8 job immagini in parallelo: inviare in gruppi da 8.
- Budget: ~25 crediti/giorno. Se il saldo Higgsfield è < 30, NON produrre: fermarsi e segnalarlo.

## Calendario settimanale (giorno di PUBBLICAZIONE = giorno dopo l'esecuzione)
| Giorno | Slot 1 (12:00) | Slot 2 (19:00) | Slot 3 (21:30) |
|---|---|---|---|
| Lunedì, Giovedì | storia | scienza/spazio | **ENIGMA** |
| Mercoledì, Sabato | storia | **TOP 5** | misteri |
| Martedì, Venerdì, Domenica | storia | scienza/spazio | misteri |
Almeno 3 Short a settimana devono essere di **spazio/scienza con foto NASA reali**.
L'esecuzione della **domenica** prepara anche la **compilation settimanale** (vedi sotto).

## Titoli (formule che funzionano, ispirate ai canali di divulgazione italiani più grandi)
- "Gli scienziati hanno **appena** scoperto…" / "La NASA ha rilevato…" / "James Webb ha visto qualcosa di **impossibile**…"
- "**Dopo** 100 / 600 / 2.000 anni, … ha **finalmente** una spiegazione" (usare solo se è vero)
- "**Perché nessuno** riesce a…" / "Ecco perché…"
- "Il libro / tempio / cibo che **NESSUNO**…" + una parola emotiva (terrificante, inquietante, impossibile, incredibile)
- Una o due parole in MAIUSCOLO, massimo un'emoji, ≤ 70 caratteri. Niente promesse false: il titolo deve essere vero.
- Notizie recenti ("appena", "nuova scoperta"): **verificare con WebSearch** su fonti serie (NASA, ESA, Nature, università,
  ANSA/Le Scienze) e citare la fonte in descrizione. Se non si trova conferma, cambiare argomento.

## Formato ENIGMA (lunedì e giovedì, slot 21:30)
- 18-25 s. Apertura: "Solo una persona su dieci risolve questo enigma." → enigma in 2-3 frasi → "Hai tre secondi."
  → tre scene brevissime con "3", "2", "1" a tutto schermo → "Scrivi la risposta nei commenti." → "La risposta è..."
  e il video riparte dall'apertura (loop: **la risposta NON si dice mai** nel video).
- Prendere l'enigma da `topics.md` (sezione Enigmi), che contiene anche la risposta: scriverla in `testi.md` con
  il consiglio di **fissarla come commento il giorno dopo**.
- Immagini: illustrative (IA consentita se serve: in quel caso etichetta).

## Compilation settimanale (esecuzione della domenica)
- Prendere gli Short consegnati negli ultimi 7 giorni (cartelle `work/consegna/`) e unirli con
  `.venv/bin/python -I compile.py work/consegna/<data>/compilation.mp4 "<titolo 1>" file1.mp4 "<titolo 2>" file2.mp4 ...`
  (formato 16:9, cartello "#n + titolo" tra un video e l'altro). Ordine: i più forti per primi.
- Titolo: "N curiosità che non sapevi: storia, misteri e scienza (settimana del GG mese)" o simile; descrizione con
  l'elenco dei capitoli (timestamp 00:00 ...) e le fonti delle immagini. Consegnarla insieme ai 3 Short del lunedì.

## Formato Top 5 (due volte a settimana)
Quando il giorno di pubblicazione (il giorno DOPO l'esecuzione) è **mercoledì o sabato**, lo Short di scienza (o quello della categoria con meno argomenti)
è una **Top 5** presa dalla sezione "Top 5" di `topics.md` (al posto dell'argomento singolo di quella categoria).
- Struttura (30-40 s, stesse regole del formato corto, senza saluto finale): apertura ("Cinque ... che non conoscevi. Resta fino al numero uno."), poi dal **numero cinque
  al numero uno**, 1-2 frasi ciascuno, il più sorprendente per ultimo; chiusura Svelarium.
- Ogni elemento inizia con la parola del numero ("Numero cinque: ...", ..., "Numero uno: ...") così l'allineamento è facile.
- 7 scene: 1 = apertura, 2-6 = numeri 5..1, 7 = chiusura (riusa l'immagine dell'apertura). 6 immagini.
- `HEAD`: scena 1 il titolo della classifica ("TOP 5", "...") ; scene 2-6 il numero grande ("#5", colore g; "#1" colore r)
  e sotto il nome dell'elemento in 2-4 parole.
- Titolo YouTube/TikTok: "TOP 5 ... 🤯 #shorts". Stessi controlli di qualità e stesse regole sui fatti.

## Giorni già coperti (aggiornare a ogni consegna)
- Fino a **lunedì 30/11/2026** compreso: pacchetti `2026-11-25/`, `9_video_misti/` (26-28/11), `2026-11-29/`, `2026-11-30/` (TikTok già programmato).
- La compilation settimanale si fa nell'esecuzione che avviene **di domenica** (calendario reale), con gli Short della settimana.
- La routine giornaliera produce per il **primo giorno non ancora coperto** (prossimo: martedì 1/12),
  poi aggiorna questa riga. Se i giorni coperti sono già 3 o più avanti, produrre comunque per il primo giorno libero.

## Formato ANIMATO (dal 27/11, piace molto all'utente: "stile Colosseo con le persone che si muovono")
Ogni giorno, da **lunedì a venerdì**, UNO dei 3 Short è animato (sabato e domenica tutti con immagini reali, per risparmiare crediti).
Il tema ruota, NON solo Roma: lun storia (qualsiasi epoca: Egitto, Grecia, Medioevo, Vichinghi, Rinascimento, guerre...),
mar misteri (navi fantasma, sparizioni, leggende), mer scienza/spazio (astronauti, missioni, scoperte storiche della scienza),
gio storia (personaggi famosi), ven misteri o "miti da sfatare". Gli altri 2 Short del giorno restano a immagini reali.
- Costo massimo ~30 crediti a Short animato: **7 immagini** `gpt_image_2_6` 9:16 (0,75 cr l'una), di cui **4 animate**
  (le scene più d'azione) con `seedance_2_0`, `mode fast`, `480p`, `duration 5`, `generate_audio false`,
  `medias [{role: start_image, value: <job immagine>}]` (5 cr l'una); le altre 3 restano immagini ferme con zoom.
  Max 6 job video in contemporanea (la voce conta): inviare 4 video + voce, poi il resto.
- Prompt immagini: "Photorealistic cinematic film still, <epoca e luogo>, <scena con persone in azione>, vertical composition,
  epic historical movie look, no text". Niente sangue, ferite, nudità. Prompt video: cosa si muove (persone, animali, folla,
  camera lenta), "Realistic motion".
- In `IMG` le clip animate vanno come `NN.mp4` (stesso numero dell'immagine): `build.py` le usa al posto della foto
  (rallenta fino a 2x per riempire la scena). L'ultima scena riusa la clip 1 per il loop.
- Controllare una griglia di fotogrammi (ffmpeg fps=0.5,tile) prima di consegnare: niente volti o cavalli deformati.
- Etichetta: immagini IA → nel testo "Contenuti alterati: Sì" (YouTube) e "contenuto IA" (TikTok, `isAigc: true` in Metricool).
- Esempio funzionante: `specs/anim_auriga.py` (l'atleta più pagato della storia).

## Procedura (una esecuzione = 3 Short)
1. `cd svelarium && bash setup.sh`
2. Leggere `topics.md`: scegliere il primo argomento **non usato** per ciascuna categoria (storia, misteri, scienza).
   Se una categoria è esaurita, aggiungere nuovi argomenti solidi alla lista prima di procedere.
3. Per ciascun argomento scrivere il testo nel **formato corto con loop** (dal 23/11):
   - **30-40 secondi** (~85-110 parole), 10-12 frasi brevi: una scena ogni 2-3 s. (Dati canale 24/11: i migliori
     sono di 45-55 s con 30-38 s di visione media; spazio/scienza e "fatto smentito" rendono di più);
   - prima frase = gancio fortissimo, e il **titolo grande è già nel primo fotogramma**;
   - **niente saluto finale** ("Seguimi su Svelarium" NO): l'ultima frase deve ricollegarsi alla prima
     (es. fine "E dopo seicento anni..." → inizio "Questo libro non lo sa leggere nessuno.");
     l'ultima scena riusa l'immagine e il titolo della prima, così il video riparte senza stacco (`TAIL = 0.25`);
   - **solo fatti consolidati**; teorie come teorie; numeri **in lettere** nel testo per la voce;
   - ogni riga di `LINES` deve iniziare con una **parola normale** (non un numero), e la parola iniziale
     non deve comparire nella riga precedente (allineamento).
4. Immagini: **prima le REALI**, l'IA solo dove non esiste niente di reale.
   Fonti raggiungibili (Wikimedia/Met/Pexels NON funzionano da qui):
   - **Library of Congress** (storia, luoghi, foto d'epoca e photochrom a colori ~1890-1900, pubblico dominio):
     `https://www.loc.gov/photos/?q=<query>&fo=json&c=20` → `image_url`; versione grande: sostituire
     `.../service/pnp/<coll>/<dir>/<id>v.jpg` con `.../master/pnp/<coll>/<dir>/<id>u.tif` (3000+ px).
     Controllare che il campo diritti dica "No known restrictions".
   - **NASA**: usare `python3 -I fetch_nasa.py <dir> <nasa_id1> <nasa_id2> ...` (salva 01.png, 02.png...).
     Cercare gli id con `https://images-api.nasa.gov/search?q=<query>&media_type=image`
     → `links[0].href` sostituendo `~medium`/`~thumb` con `~orig`.
   - **Yale/IIIF e altre biblioteche** (manoscritti, documenti): manifest IIIF → `<service>/full/!2000,2000/0/default.jpg`.
   - **Europeana**: `python3 -I fetch_europeana.py <dir> "<query>" <indici> ["&qf=DATA_PROVIDER:%22Rijksmuseum%22"]`
     (stampa titolo, fornitore e licenza da citare). Rijksmuseum e SMK hanno moltissimo materiale storico in pubblico dominio.
     Endpoint: `https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=<q>&reusability=open&media=true`
     → `edmIsShownBy`; usare solo licenze PD/CC0/CC-BY (citare l'autore in descrizione se CC-BY).
   - Se servono comunque immagini IA: Higgsfield `gpt_image_2_6` 9:16 (prompt in inglese, "photorealistic
     cinematic ..., no text"); in quel caso nel video ci sono immagini IA e l'etichetta va messa.
   `build.py` ritaglia da solo qualsiasi formato a 9:16: il ritaglio e lo zoom seguono il punto (fx, fy) di `SCENE_IMG`
   (0 = sinistra/alto, 1 = destra/basso) → per immagini orizzontali puntare fx sul soggetto.
   Se il titolo copre un volto, nello spec: `HEAD_Y = {scena: 1060}` sposta il titolo in basso (sopra i sottotitoli).
   Attenzione alle licenze: ESA/ESO/Hubble sono spesso CC BY 4.0 (citare l'autore); Library of Congress oggi può
   bloccare con verifica anti-bot (non aggirarla: usare altre fonti); Wellcome Collection (IIIF) è CC BY 4.0.
   Nella descrizione indicare la fonte delle immagini reali (es. "Immagini: Library of Congress, NASA").
5. Generare la voce (un'unica richiesta per Short). **Rileggere il testo prima di inviarlo** (refusi = credito sprecato).
6. Scaricare immagini in `work/<slug>/img/01.png..06.png` e voce in `work/<slug>/voice.mp3`.
7. Allineamento: `HF_HUB_CACHE=$PWD/hfcache .venv/bin/python -I align.py work/<slug>/voice.mp3 work/<slug>/words.json`
8. Scrivere `specs/<data>_<slug>.py` (vedi esempi in `specs/`): `LINES` (scena, testo parlato, sottotitolo con `|`, 0),
   `HEAD` (8 scene: titoli grandi, 2 righe, colori w/g/r/c), `SCENE_IMG` (scena -> (img, fx, fy[, z0, z1])), `SONG`
   (`output005.mp3`, `output008.mp3`, `output012.mp3`). I titoli non devono svelare la risposta prima della voce.
   Usare solo caratteri presenti nel font (niente frecce/simboli speciali).
9. Build: `SPEC=specs/<file>.py IMG=work/<slug>/img VOICE=work/<slug>/voice.mp3 WORDS=work/<slug>/words.json OUT=work/<slug>/out .venv/bin/python -I build.py`
10. **Controllo qualità**: estrarre un fotogramma per scena e guardarli. Verificare: durata 28-45 s, primo e ultimo fotogramma uguali (loop),
    titoli leggibili, sottotitoli corretti e a tempo, immagini senza difetti evidenti. Se un controllo fallisce
    e non si riesce a correggere, **non pubblicare** quello Short.
11. **TikTok: programmare IO in Metricool** (dal 24/11, richiesta dell'utente) solo rete `tiktok`, brand `8287937`, con `tiktokData.title`,
    `isAigc false` (immagini reali), agli orari del calendario. Video caricati prima con Higgsfield media_upload (URL cloudfront).
    **YouTube: NON programmare** (lo carica l'utente a mano).
    Copiare i 3 video in `work/consegna/<data>/` con nomi chiari (es. `1_storia_pompei.mp4`).
12. Scrivere `work/consegna/<data>/testi.md` con, per ogni Short: orario consigliato (storia 12:00, scienza 19:00,
    misteri 21:30), titolo YouTube (≤ 70 caratteri, con " #shorts"), titolo TikTok (senza #shorts), descrizione
    (riassunto + "👉 Iscriviti a Svelarium: ogni giorno un segreto svelato." + "Voce generata con IA. Immagini: <fonti>" (aggiungere "e IA" se ci sono immagini IA) + 6-7 hashtag), tag YouTube, e il promemoria:
    se il video contiene immagini IA realistiche → "Contenuti alterati: Sì" (YouTube) / "contenuto IA" (TikTok);
    se le immagini sono tutte reali e solo la voce narrante è sintetica (voce generica, non di una persona reale)
    l'etichetta non è richiesta da YouTube.
13. Inviare all'utente i 3 video e `testi.md` con SendUserFile (status proactive), più un breve messaggio in chat
    con titoli e orari consigliati. Evitare argomenti simili a meno di 3-4 giorni di distanza da quelli recenti.
14. Segnare gli argomenti usati in `topics.md` (data + titolo), committare spec e topics, push sul ramo.
15. Riepilogo finale: 3 titoli, orari, crediti spesi, eventuali problemi.
