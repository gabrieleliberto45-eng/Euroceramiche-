import re, base64, sys, os
root = sys.argv[1]; out = sys.argv[2]
s = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
def uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(root, path), 'rb').read()).decode()
# niente preload/srcset: un solo file per immagine
s = re.sub(r'<link rel="preload"[^>]*>\n?', '', s)
s = re.sub(r'\s(?:srcset|sizes)="[^"]*"', '', s)
s = re.sub(r'url\((fonts/[^)]+\.woff2)\)', lambda m: f'url({uri(m.group(1), "font/woff2")})', s)
s = re.sub(r'src="(img/[^"]+\.webp)"', lambda m: f'src="{uri(m.group(1), "image/webp")}"', s)
s = s.replace('<meta property="og:image" content="img/hero.webp">', '')
s = s.replace('"image": "img/hero.webp",', '')
s = s.replace('href="privacy.html"', 'href="#"')
open(out, 'w', encoding='utf-8').write(s)
print(out, os.path.getsize(out) // 1024, 'KB', 'leftover refs:', re.findall(r'(?:src|href)="(?:img|fonts)/[^"]*"', s))
