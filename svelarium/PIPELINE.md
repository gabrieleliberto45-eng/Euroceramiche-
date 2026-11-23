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

## Procedura (una esecuzione = 3 Short)
1. `cd svelarium && bash setup.sh`
2. Leggere `topics.md`: scegliere il primo argomento **non usato** per ciascuna categoria (storia, misteri, scienza).
   Se una categoria è esaurita, aggiungere nuovi argomenti solidi alla lista prima di procedere.
3. Per ciascun argomento scrivere il testo nel **formato corto con loop** (dal 23/11):
   - **22-30 secondi** (~60-80 parole), 8-9 frasi brevi: una scena ogni 2-3 s;
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
   - **NASA** (scienza/spazio, pubblico dominio): `https://images-api.nasa.gov/search?q=<query>&media_type=image`
     → `links[0].href` sostituendo `~medium`/`~thumb` con `~orig`.
   - **Yale/IIIF e altre biblioteche** (manoscritti, documenti): manifest IIIF → `<service>/full/!2000,2000/0/default.jpg`.
   - **Europeana** (musei europei): `https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=<q>&reusability=open&media=true`
     → `edmIsShownBy`; usare solo licenze PD/CC0/CC-BY (citare l'autore in descrizione se CC-BY).
   - Se servono comunque immagini IA: Higgsfield `gpt_image_2_6` 9:16 (prompt in inglese, "photorealistic
     cinematic ..., no text"); in quel caso nel video ci sono immagini IA e l'etichetta va messa.
   `build.py` ritaglia da solo qualsiasi formato a 9:16 (riempimento al centro, poi zoom).
   Nella descrizione indicare la fonte delle immagini reali (es. "Immagini: Library of Congress, NASA").
5. Generare la voce (un'unica richiesta per Short). **Rileggere il testo prima di inviarlo** (refusi = credito sprecato).
6. Scaricare immagini in `work/<slug>/img/01.png..06.png` e voce in `work/<slug>/voice.mp3`.
7. Allineamento: `HF_HUB_CACHE=$PWD/hfcache .venv/bin/python -I align.py work/<slug>/voice.mp3 work/<slug>/words.json`
8. Scrivere `specs/<data>_<slug>.py` (vedi esempi in `specs/`): `LINES` (scena, testo parlato, sottotitolo con `|`, 0),
   `HEAD` (8 scene: titoli grandi, 2 righe, colori w/g/r/c), `SCENE_IMG` (scena -> (img, fx, fy[, z0, z1])), `SONG`
   (`output005.mp3`, `output008.mp3`, `output012.mp3`). I titoli non devono svelare la risposta prima della voce.
   Usare solo caratteri presenti nel font (niente frecce/simboli speciali).
9. Build: `SPEC=specs/<file>.py IMG=work/<slug>/img VOICE=work/<slug>/voice.mp3 WORDS=work/<slug>/words.json OUT=work/<slug>/out .venv/bin/python -I build.py`
10. **Controllo qualità**: estrarre un fotogramma per scena e guardarli. Verificare: durata 20-35 s, primo e ultimo fotogramma uguali (loop),
    titoli leggibili, sottotitoli corretti e a tempo, immagini senza difetti evidenti. Se un controllo fallisce
    e non si riesce a correggere, **non pubblicare** quello Short.
11. **NON programmare in Metricool** (dal 23/11 l'utente carica a mano: i video caricati via API rendevano meno).
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
