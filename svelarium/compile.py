"""Compilation settimanale: unisce gli Short verticali in un video orizzontale 16:9 (1920x1080).

Ogni Short viene messo al centro, a tutta altezza, su uno sfondo sfocato ricavato dal video stesso.
Tra un video e l'altro: un cartello di 2 s con il numero e il titolo.

Uso: python compile.py <out.mp4> "<titolo 1>" short1.mp4 "<titolo 2>" short2.mp4 ...
"""
import os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
BOLD = f"{D}/assets/fonts/BeVietnamPro-Bold.ttf"
W, H, FPS = 1920, 1080, 30

out, rest = sys.argv[1], sys.argv[2:]
pairs = list(zip(rest[0::2], rest[1::2]))
tmp = tempfile.mkdtemp()
parts = []


def card(i, title):
    im = Image.new("RGB", (W, H), (12, 10, 8)); d = ImageDraw.Draw(im)
    n = ImageFont.truetype(BOLD, 220); t = ImageFont.truetype(BOLD, 72)
    s = f"#{i}"; d.text(((W - d.textlength(s, font=n)) / 2, 260), s, font=n, fill=(242, 181, 68))
    while d.textlength(title, font=t) > W - 200 and t.size > 36: t = ImageFont.truetype(BOLD, t.size - 4)
    d.text(((W - d.textlength(title, font=t)) / 2, 600), title, font=t, fill=(250, 245, 235))
    p = f"{tmp}/card{i}.png"; im.save(p)
    v = f"{tmp}/card{i}.mp4"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-t", "2", "-i", p, "-f", "lavfi", "-t", "2",
                    "-i", "anullsrc=r=44100:cl=stereo", "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264",
                    "-c:a", "aac", "-shortest", v], check=True)
    return v


for i, (title, src) in enumerate(pairs, 1):
    parts.append(card(i, title))
    v = f"{tmp}/part{i}.mp4"
    fc = (f"[0:v]split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=40,eq=brightness=-0.15[bg];"
          f"[b]scale=-2:{H}[fg];[bg][fg]overlay=(W-w)/2:0,fps={FPS},format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[v]", "-map", "0:a",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-ar", "44100", "-ac", "2", v], check=True)
    parts.append(v)

lst = f"{tmp}/list.txt"
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264",
                "-preset", "medium", "-crf", "20", "-c:a", "aac", "-movflags", "+faststart", out], check=True)
print("ok", out)
