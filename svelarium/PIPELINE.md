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
- Struttura (45-58 s): apertura ("Cinque ... che non conoscevi. Resta fino al numero uno."), poi dal **numero cinque
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
3. Per ciascun argomento scrivere il testo (35-50 s, ~110-140 parole):
   - apertura fortissima nella prima frase (domanda o fatto sorprendente);
   - **solo fatti consolidati**; teorie presentate come teorie ("secondo alcuni studiosi"); niente cifre inventate;
   - numeri scritti **in lettere** nel testo per la voce (es. "milletrecentoquarantasette");
   - ogni riga di `LINES` deve iniziare con una **parola normale** (non un numero), altrimenti l'allineamento fallisce;
   - chiusura fissa: "Seguimi su Svelarium: ogni giorno, un segreto svelato."
   - per i misteri, prima della chiusura: "Tu cosa ne pensi? Scrivilo nei commenti."
4. Generare 6 immagini per Short (prompt in inglese, "photorealistic cinematic ..., documentary film still, no text";
   niente gore, niente persone reali riconoscibili, niente loghi).
5. Generare la voce (un'unica richiesta per Short). **Rileggere il testo prima di inviarlo** (refusi = credito sprecato).
6. Scaricare immagini in `work/<slug>/img/01.png..06.png` e voce in `work/<slug>/voice.mp3`.
7. Allineamento: `HF_HUB_CACHE=$PWD/hfcache .venv/bin/python -I align.py work/<slug>/voice.mp3 work/<slug>/words.json`
8. Scrivere `specs/<data>_<slug>.py` (vedi esempi in `specs/`): `LINES` (scena, testo parlato, sottotitolo con `|`, 0),
   `HEAD` (8 scene: titoli grandi, 2 righe, colori w/g/r/c), `SCENE_IMG` (scena -> (img, fx, fy[, z0, z1])), `SONG`
   (`output005.mp3`, `output008.mp3`, `output012.mp3`). I titoli non devono svelare la risposta prima della voce.
   Usare solo caratteri presenti nel font (niente frecce/simboli speciali).
9. Build: `SPEC=specs/<file>.py IMG=work/<slug>/img VOICE=work/<slug>/voice.mp3 WORDS=work/<slug>/words.json OUT=work/<slug>/out .venv/bin/python -I build.py`
10. **Controllo qualità**: estrarre 8 fotogrammi (uno per scena) e guardarli. Verificare: durata 30-59 s,
    titoli leggibili, sottotitoli corretti e a tempo, immagini senza difetti evidenti. Se un controllo fallisce
    e non si riesce a correggere, **non pubblicare** quello Short.
11. **NON programmare in Metricool** (dal 23/11 l'utente carica a mano: i video caricati via API rendevano meno).
    Copiare i 3 video in `work/consegna/<data>/` con nomi chiari (es. `1_storia_pompei.mp4`).
12. Scrivere `work/consegna/<data>/testi.md` con, per ogni Short: orario consigliato (storia 12:00, scienza 19:00,
    misteri 21:30), titolo YouTube (≤ 70 caratteri, con " #shorts"), titolo TikTok (senza #shorts), descrizione
    (riassunto + "👉 Iscriviti a Svelarium: ogni giorno un segreto svelato." + "🎨 Immagini e voce generate con
    intelligenza artificiale a scopo illustrativo." + 6-7 hashtag), tag YouTube, e il promemoria
    "Contenuti alterati: Sì" (YouTube) / "contenuto IA" (TikTok).
13. Inviare all'utente i 3 video e `testi.md` con SendUserFile (status proactive), più un breve messaggio in chat
    con titoli e orari consigliati. Evitare argomenti simili a meno di 3-4 giorni di distanza da quelli recenti.
14. Segnare gli argomenti usati in `topics.md` (data + titolo), committare spec e topics, push sul ramo.
15. Riepilogo finale: 3 titoli, orari, crediti spesi, eventuali problemi.
