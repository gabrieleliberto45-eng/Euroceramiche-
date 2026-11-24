"""Cerca su Europeana (solo licenze aperte) e scarica i risultati scelti.
Uso: fetch_europeana.py <dir> "<query>" <indici separati da virgola> [extra_qf]
Salva <dir>/eNN.png e stampa titolo, fornitore, licenza (per la descrizione)."""
import json, os, sys, urllib.parse, urllib.request
UA = {"User-Agent": "SvelariumBot/1.0 (educational shorts)"}
out, q, idx = sys.argv[1], sys.argv[2], [int(i) for i in sys.argv[3].split(",")]
extra = sys.argv[4] if len(sys.argv) > 4 else ""
os.makedirs(out, exist_ok=True)
url = ("https://api.europeana.eu/record/v2/search.json?wskey=api2demo&reusability=open&media=true&type=IMAGE&rows=20&query="
       + urllib.parse.quote(q) + extra)
items = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)).get("items", [])
n = len([f for f in os.listdir(out) if f.startswith("e")])
for i in idx:
    it = items[i]; src = (it.get("edmIsShownBy") or [""])[0]
    if "googleusercontent" in src or "ggpht" in src:
        src = src.split("=")[0] + "=s0"
    n += 1; dst = f"{out}/e{n:02d}.png"
    try:
        data = urllib.request.urlopen(urllib.request.Request(src, headers=UA), timeout=120).read()
        open(dst + ".src", "wb").write(data)
        os.system(f"ffmpeg -loglevel error -y -i '{dst}.src' -vf \"scale='min(2400,iw)':-2\" '{dst}' && rm '{dst}.src'")
        print(dst, "|", (it.get("title") or [""])[0][:60], "|", (it.get("dataProvider") or [""])[0], "|", (it.get("rights") or [""])[0])
    except Exception as e:
        print("FAIL", i, src[:80], e)
