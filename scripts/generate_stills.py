#!/usr/bin/env python3
"""Génère une image par plan avec Nano Banana (API Gemini) dans stills/clip-XX.png.

Clé lue dans la variable d'environnement GEMINI_API_KEY.
Le plan 1 sert d'image de référence aux plans suivants pour garder le même personnage.
Usage : python3 scripts/generate_stills.py [numéros de plans…]   (défaut : tous)
"""
import base64, json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL = os.environ.get("NANO_BANANA_MODEL", "gemini-2.5-flash-image")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
KEY = os.environ.get("GEMINI_API_KEY")
if not KEY:
    sys.exit("GEMINI_API_KEY absente : ajoutez-la dans les variables de l'environnement.")

clips = json.loads((ROOT / "prompts/clips.json").read_text(encoding="utf-8"))
wanted = {int(a) for a in sys.argv[1:]} or {c["clip"] for c in clips}
out = ROOT / "stills"
out.mkdir(exist_ok=True)
ref = out / "clip-01.png"

def generate(prompt, ref_png=None):
    parts = [{"text": prompt}]
    if ref_png:
        parts.insert(0, {"inline_data": {"mime_type": "image/png", "data": base64.b64encode(ref_png.read_bytes()).decode()}})
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "16:9"}}}
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json", "x-goog-api-key": KEY})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 3:
                time.sleep(2 ** (attempt + 2)); continue
            sys.exit(f"Erreur API {e.code} : {e.read().decode()[:500]}")
    for p in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        blob = p.get("inline_data") or p.get("inlineData")
        if blob:
            return base64.b64decode(blob["data"])
    sys.exit(f"Pas d'image dans la réponse : {json.dumps(data)[:500]}")

for c in sorted(clips, key=lambda c: c["clip"]):
    if c["clip"] not in wanted:
        continue
    n = f"{c['clip']:02d}"
    # Le prompt vidéo décrit 8 s d'action ; on demande l'image clé du plan.
    prompt = ("Single cinematic film still, 16:9, photorealistic, key frame of this commercial shot "
              "(ignore sound and camera-move directions): " + c["prompt"])
    use_ref = c["clip"] != 1 and ref.exists() and c["clip"] != 2
    if use_ref:
        prompt = "Keep exactly the same young man as in the reference image (face, curly brown hair, light grey hoodie). " + prompt
    print(f"Plan {n} : génération…", flush=True)
    (out / f"clip-{n}.png").write_bytes(generate(prompt, ref if use_ref else None))
    print(f"Plan {n} : stills/clip-{n}.png")
