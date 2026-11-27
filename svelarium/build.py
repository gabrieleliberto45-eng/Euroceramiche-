"""Svelarium Short builder: realistic images + ElevenLabs voice + word-synced subtitles + headlines.

Usage: SPEC=specs/x.py IMG=<images dir> VOICE=<voice.mp3> WORDS=<words.json> OUT=<out dir> python build.py
Spec defines LINES, HEAD, SCENE_IMG and optionally SONG (file name in assets/songs).
"""
import json, os, re, subprocess, unicodedata
from PIL import Image, ImageDraw, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
FONTS = f"{D}/assets/fonts"
BOLD = f"{FONTS}/BeVietnamPro-Bold.ttf"
IMG, OUT = os.environ["IMG"], os.environ["OUT"]
SONG = "output005.mp3"
COL = {"w": (250, 245, 235), "g": (242, 181, 68), "r": (230, 72, 50), "c": (150, 220, 255)}
W, H, FPS = 1080, 1920, 30
SCENE_IMG = {k: (k, 0.5, 0.5) for k in range(1, 10)}
exec(open(os.environ["SPEC"]).read(), {"D": D}, ns := {})
LINES, HEAD = ns["LINES"], ns["HEAD"]
SCENE_IMG.update(ns.get("SCENE_IMG", {}))
SONG = f"{D}/assets/songs/" + os.path.basename(ns.get("SONG", SONG))
os.makedirs(OUT, exist_ok=True)
NS = max(HEAD)

norm = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode())
words = json.load(open(os.environ["WORDS"]))
wn = [norm(w[0]) for w in words]
starts_idx, pos = [], 0
for _, spoken, _, _ in LINES:
    first = norm(spoken.split()[0].split("'")[0])
    window = range(pos, min(pos + 40, len(wn)))
    hit = next((i for i in window if wn[i] == first), None)
    if hit is None:  # whisper may mangle a word ("Negli scavi" -> "Nell'escavi"): fall back to a prefix match
        hit = next((i for i in window if len(first) >= 3 and wn[i][:3] == first[:3]), None)
    if hit is None:  # last resort: fuzzy match of the first two words
        import difflib
        two = norm("".join(spoken.split()[:2]))
        scored = [(difflib.SequenceMatcher(None, two, wn[i] + (wn[i + 1] if i + 1 < len(wn) else "")).ratio(), i) for i in window]
        best = max(scored, default=(0, None))
        hit = best[1] if best[0] >= 0.7 else None
    if hit is None:
        raise SystemExit(f"alignment failed at line starting {spoken!r}: rephrase so it starts with a plain word")
    # skip most of this line's own words, so a repeated word ("tre secondi... Tre") is not matched too early
    starts_idx.append(hit); pos = hit + max(1, len(spoken.split()) - 1)
timings = []
for k, si in enumerate(starts_idx):
    end_i = (starts_idx[k + 1] - 1) if k + 1 < len(starts_idx) else len(words) - 1
    timings.append((max(0.0, words[si][1] - 0.08), words[end_i][2]))
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", os.environ["VOICE"], "-af",
                "highpass=f=60,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80,apad=pad_dur=0.6",
                "-ar", "44100", f"{OUT}/voice.wav"], check=True)
TOTAL = words[-1][2] + float(ns.get("TAIL", 0.6))

# --- subtitles (ASS) ------------------------------------------------------------
def ts(x):
    h, r = divmod(x, 3600); m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"
cues = []
for (a, b), (_, _, sub, pause) in zip(timings, LINES):
    a, b = a + 0.05, b - 0.05
    parts = [p.strip() for p in sub.split("|") if p.strip()]
    if not parts: continue
    tot = sum(len(p) for p in parts); x = a
    for p in parts:
        e = x + (b - a) * len(p) / tot; cues.append([x, e, p]); x = e
for i in range(len(cues) - 1):  # hold until next cue when the gap is short
    if cues[i + 1][0] - cues[i][1] < 0.5: cues[i][1] = cues[i + 1][0]
hl = lambda p: re.sub(r"\b([A-ZÀ-ÖØ-Þ][A-ZÀ-ÖØ-Þ]{3,}(?: [A-ZÀ-ÖØ-Þ]{2,})*)\b", r"{\\c&H44B5F2&}\1{\\c}", p)
ass = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Sub,Be Vietnam Pro,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,7,3,2,70,70,360,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for s, e, p in cues:
    ass.append(f"Dialogue: 0,{ts(s)},{ts(e)},Sub,,0,0,0,,{{\\fad(60,40)\\t(0,120,\\fscx108\\fscy108)\\t(120,220,\\fscx100\\fscy100)}}{hl(p)}")
open(f"{OUT}/subs.ass", "w").write("\n".join(ass) + "\n")

# --- headline overlays (top gradient + big text) ----------------------------------
def overlay(scene):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for y in range(760):
        d.line([(0, y), (W, y)], fill=(0, 0, 0, int(190 * (1 - y / 760) ** 1.4)))
    for y in range(1200, H):
        d.line([(0, y), (W, y)], fill=(0, 0, 0, int(170 * ((y - 1200) / (H - 1200)) ** 1.6)))
    y = ns.get("HEAD_Y", {}).get(scene, 190)
    for text, size, c in HEAD[scene]:
        f = ImageFont.truetype(BOLD, size)
        while d.textlength(text, font=f) > W - 100: size -= 4; f = ImageFont.truetype(BOLD, size)
        d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=COL[c], stroke_width=max(4, size // 16), stroke_fill=(10, 8, 6))
        y += int(size * 1.18)
    p = f"{OUT}/head{scene}.png"; im.save(p); return p

# --- scene timeline from the first line of each scene -----------------------------
starts = {}
for (a, _), (scene, *_r) in zip(timings, LINES): starts.setdefault(scene, a)
bounds = [0.0] + [starts[s] for s in range(2, NS + 1)] + [TOTAL]
inputs, fl = [], []
for k in range(NS):
    dur = bounds[k + 1] - bounds[k]; n = int(round(dur * FPS))
    im_no, fx, fy, *zz = SCENE_IMG[k + 1]
    mp4 = f"{IMG}/{im_no:02d}.mp4"
    if os.path.exists(mp4):  # animated scene: the clip, slowed down (at most 2x) to fill the scene, then looped
        clen = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp4],
                                    capture_output=True, text=True).stdout.strip() or 5)
        slow = min(2.0, max(1.0, dur / clen))
        inputs += ["-stream_loop", "-1", "-i", mp4, "-i", overlay(k + 1)]
        fl.append(f"[{2 * k}:v]setpts={slow:.3f}*(PTS-STARTPTS),scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
                  f"crop={W}:{H}:(iw-ow)*{fx}:(ih-oh)*{fy},fps={FPS},trim=duration={dur:.3f},setpts=PTS-STARTPTS,setsar=1[b{k}];"
                  f"[{2 * k + 1}:v]loop=loop=-1:size=1,trim=duration={dur:.3f},fps={FPS},setpts=PTS-STARTPTS[o{k}];"
                  f"[b{k}][o{k}]overlay=0:0:shortest=1[v{k}]")
        continue
    inputs += ["-i", f"{IMG}/{im_no:02d}.png", "-i", overlay(k + 1)]
    z0, z1 = zz if zz else ((1.0, 1.12) if k % 2 == 0 else (1.12, 1.0))
    z = f"{z0}+({z1 - z0:.3f})*on/{n}"
    fl.append(f"[{2 * k}:v]scale=2160:3840:force_original_aspect_ratio=increase:flags=lanczos,crop=2160:3840:(iw-ow)*{fx}:(ih-oh)*{fy},zoompan=z='{z}':x='(iw-iw/zoom)*{fx}':y='(ih-ih/zoom)*{fy}':d={n}:s={W}x{H}:fps={FPS},setsar=1[b{k}];"
              f"[{2 * k + 1}:v]loop=loop=-1:size=1,trim=duration={dur:.3f},fps={FPS},setpts=PTS-STARTPTS[o{k}];"
              f"[b{k}][o{k}]overlay=0:0:shortest=1[v{k}]")
fl.append("".join(f"[v{k}]" for k in range(NS)) + f"concat=n={NS}:v=1:a=0,subtitles={OUT}/subs.ass:fontsdir={FONTS}[vid]")
nv = 2 * NS
fl.append(f"[{nv + 1}:a]volume=0.10,afade=t=in:d=0.3,afade=t=out:st={TOTAL - 0.6}:d=0.6[bgm];[{nv}:a][bgm]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aud]")
cmd = ["ffmpeg", "-loglevel", "error", "-y", *inputs, "-i", f"{OUT}/voice.wav", "-stream_loop", "-1", "-i", SONG,
       "-filter_complex", ";".join(fl), "-map", "[vid]", "-map", "[aud]", "-t", f"{TOTAL:.3f}",
       "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
       "-movflags", "+faststart", f"{OUT}/short.mp4"]
subprocess.run(cmd, check=True)
print(json.dumps({"duration": round(TOTAL, 2), "scene_starts": [round(b, 2) for b in bounds]}))
