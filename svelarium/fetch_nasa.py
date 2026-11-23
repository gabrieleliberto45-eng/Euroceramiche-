"""Scarica immagini NASA (pubblico dominio) per nasa_id, preferendo ~large poi ~orig. Uso: fetch_nasa.py <dir> id1 id2 ..."""
import json, os, sys, urllib.request
UA = {"User-Agent": "SvelariumBot/1.0 (educational shorts)"}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for i, nid in enumerate(sys.argv[2:], 1):
    r = urllib.request.urlopen(urllib.request.Request(f"https://images-api.nasa.gov/asset/{nid}", headers=UA), timeout=60)
    hrefs = [x["href"] for x in json.load(r)["collection"]["items"]]
    imgs = [h for h in hrefs if h.lower().endswith((".jpg", ".jpeg", ".png", ".tif"))]
    pick = next((h for k in ("~large", "~orig", "~medium") for h in imgs if k in h and not h.endswith(".tif")), imgs[0])
    pick = pick.replace("http://", "https://").replace(" ", "%20")
    dst = f"{out}/{i:02d}.png"
    data = urllib.request.urlopen(urllib.request.Request(pick, headers=UA), timeout=120).read()
    tmp = dst + ".src"; open(tmp, "wb").write(data)
    os.system(f"ffmpeg -loglevel error -y -i '{tmp}' -vf \"scale='min(2400,iw)':-2\" '{dst}' && rm '{tmp}'")
    print(i, nid, pick.rsplit("/", 1)[-1])
