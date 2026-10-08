#!/usr/bin/env python3
"""Régénère prompts/clip-XX.txt et README.md à partir de prompts/clips.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
clips = json.loads((ROOT / "prompts/clips.json").read_text(encoding="utf-8"))

md = [
    "# Spot publicitaire « Le Cocon » — bibliothèque",
    "",
    "Spot de 64 secondes, 8 clips de 8 s générés par IA vidéo (prompts en anglais, prêts à copier-coller).",
    "",
    "| # | Début | Titre | Prompt | Rush attendu |",
    "|---|---|---|---|---|",
]
for c in clips:
    n = f"{c['clip']:02d}"
    (ROOT / f"prompts/clip-{n}.txt").write_text(c["prompt"] + "\n", encoding="utf-8")
    md.append(f"| {c['clip']} | {c['start']} | {c['title']} | [`prompts/clip-{n}.txt`](prompts/clip-{n}.txt) | `clips/clip-{n}.mp4` |")

md += [
    "",
    "## Montage",
    "",
    "1. Générez chaque clip avec son prompt et déposez le fichier dans `clips/` sous le nom `clip-01.mp4` … `clip-08.mp4`.",
    "2. Lancez `./scripts/montage.sh`.",
    "3. Le spot est écrit dans `output/spot-le-cocon.mp4` (1920×1080, 24 i/s, H.264 + AAC, 64 s).",
    "",
    "Si un rush manque, le script le remplace par un carton (animatique) indiquant le numéro, le titre et le timecode du plan : on peut donc monter et vérifier le rythme avant d'avoir tous les clips. Chaque rush est recadré au format 16:9, ramené à 8 s exactement, et son son est normalisé (fondu de 0,15 s en entrée et en sortie pour éviter les clics aux coupes). Un rush sans piste audio reçoit un silence. Le spot commence par un fondu depuis le noir et se termine par un fondu au noir.",
    "",
    "Après modification de `prompts/clips.json`, lancez `python3 scripts/build_prompts.py` pour régénérer les fichiers `.txt` et ce README.",
    "",
    "## Prompts",
    "",
]
for c in clips:
    md += [f"### Clip {c['clip']} · {c['start']} – {c['title']}", "", "```", c["prompt"], "```", ""]
md += [
    "## Continuité (à garder identique d'un clip à l'autre)",
    "",
    "- **Personnage** : jeune homme français de 18 ans, cheveux bruns courts et bouclés, sweat à capuche gris clair, sac à dos noir (clips 3, 7, 8).",
    "- **Le Cocon** : dôme de lecture en bois de 4 m, panneaux de contreplaqué de bouleau clair cintrés, nervures en chêne, porte arrondie, intérieur en feutre acoustique gris foncé, anneau LED chaud, fauteuil inclinable en laine terracotta avec écran tactile dans l'accoudoir.",
    "- **Bibliothèque** : moderne et lumineuse, grandes fenêtres, étagères en bois, longues tables en bois, lumière dorée.",
    "- **Bibliothécaire** (clip 8) : femme d'une quarantaine d'années, cheveux bruns mi-longs, pull vert foncé.",
    "- **Seul texte à l'écran** : « Lis autrement, vis l'histoire » (clip 2). Aucun logo nulle part.",
    "",
    "## Arc sonore",
    "",
    "1–2 : pas de musique, bruits de chambre → carillon de notification · 3–4 : piano chaleureux, cordes · 5 : le bruit extérieur s'efface · 6 : paysage sonore immersif · 7–8 : musique entraînante jusqu'à l'accord final.",
    "",
]
(ROOT / "README.md").write_text("\n".join(md), encoding="utf-8")
print("README.md et prompts/clip-XX.txt régénérés.")
