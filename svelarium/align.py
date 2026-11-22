import json, sys
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = m.transcribe(sys.argv[1], language="it", word_timestamps=True)
words = [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words]
json.dump(words, open(sys.argv[2], "w"), ensure_ascii=False); print(len(words)); print(" ".join(w[0] for w in words))
