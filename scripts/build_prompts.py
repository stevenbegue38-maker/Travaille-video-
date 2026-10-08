#!/usr/bin/env python3
"""Régénère prompts/clip-XX.txt, prompts/image-XX.txt et README.md à partir de prompts/clips.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
clips = json.loads((ROOT / "prompts/clips.json").read_text(encoding="utf-8"))
REFERENCE = ("Character reference sheet, photorealistic, 35mm film look, neutral soft studio light, plain light grey background, 16:9. "
             "The same person shown three times side by side: front view, three-quarter view and profile, head and shoulders. "
             "A French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, "
             "wearing a plain light grey hoodie with no print. Calm neutral expression. No text, no logos.")
(ROOT / "prompts/reference-personnage.txt").write_text(REFERENCE + "\n", encoding="utf-8")
videos = [c for c in clips if c["mode"] == "video"]
images = [c for c in clips if c["mode"] == "image"]
nums = lambda cs: ", ".join(str(c["clip"]) for c in cs)

md = [
    "# Spot publicitaire « Le Cocon » — bibliothèque",
    "",
    "Spot de 64 secondes, 8 clips de 8 s générés par IA vidéo (prompts en anglais, prêts à copier-coller).",
    "",
    "| # | Début | Titre | Ce soir | Prompt vidéo | Prompt image | Fichier à déposer |",
    "|---|---|---|---|---|---|---|",
]
for c in clips:
    n = f"{c['clip']:02d}"
    (ROOT / f"prompts/clip-{n}.txt").write_text(c["prompt"] + "\n", encoding="utf-8")
    (ROOT / f"prompts/image-{n}.txt").write_text(c["still"] + "\n", encoding="utf-8")
    mode, fichier = ("vidéo Flow", f"clips/clip-{n}.mp4") if c["mode"] == "video" else ("image animée", f"stills/clip-{n}.png")
    md.append(f"| {c['clip']} | {c['start']} | {c['title']} | {mode} | [`clip-{n}.txt`](prompts/clip-{n}.txt) | [`image-{n}.txt`](prompts/image-{n}.txt) | `{fichier}` |")

md += [
    "",
    "## Tout faire en une soirée, gratuitement",
    "",
    "Google Flow gratuit donne environ 50 crédits par jour et un clip Veo 3.1 Lite en coûte 10 : 5 vidéos par soir. "
    f"Les plans {nums(videos)} (ceux qui ont le plus d'action) sont donc faits en vidéo, les plans {nums(images)} en image fixe animée par un zoom lent au montage.",
    "",
    "**Règle d'or : aucun abonnement, aucune carte bancaire.** Si une page demande un paiement, on s'arrête.",
    "",
    "1. **Personnage de référence** (app Gemini gratuite, gemini.google.com) : collez [`prompts/reference-personnage.txt`](prompts/reference-personnage.txt), gardez l'image dont le visage vous plaît.",
    "2. **Les 8 images clés** (app Gemini) : pour chaque plan, joignez l'image de référence et collez « Keep exactly the same young man as in the attached image (face, hair, clothes). » suivi du contenu de `prompts/image-XX.txt`. "
    f"Enregistrez les images des plans {nums(images)} sous `stills/clip-XX.png` (les autres servent de première image à Flow).",
    "3. **Les vidéos** (labs.google/flow, compte Google personnel) : vérifiez le solde (~50 crédits) sous la photo de profil, choisissez **Veo 3.1 Lite**, format 16:9, 8 s. "
    f"Pour chacun des plans {nums(videos)} : mode « Frames to Video » avec l'image clé du plan en première image, collez `prompts/clip-XX.txt`, générez **une seule fois**, téléchargez sous `clips/clip-XX.mp4`. "
    "Si le solde ne suffit plus, le plan restant passe en image animée (déposez simplement `stills/clip-XX.png`).",
    "4. **Montage** : `./scripts/montage.sh` → `output/spot-le-cocon.mp4` (1920×1080, 24 i/s, H.264 + AAC, 64 s).",
    "",
    "Usage commercial : les conditions de Google pour l'offre gratuite de Flow ne le confirment pas clairement, et un filigrane visible peut être ajouté selon le pays. Vérifiez avant toute diffusion payante.",
    "",
    "## Montage",
    "",
    "Pour chaque plan, le script prend la vidéo `clips/clip-XX.mp4`, sinon l'image `stills/clip-XX.png` (zoom lent de 8 s), sinon un carton d'animatique indiquant le numéro, le titre et le timecode du plan : on peut monter et vérifier le rythme avant d'avoir tous les clips. "
    "Chaque rush est recadré au format 16:9, ramené à 8 s exactement, et son son est normalisé (fondu de 0,15 s en entrée et en sortie). Un rush sans piste audio reçoit un silence. "
    "Le sous-titre « caption » d'un plan (clip 2 : « Lis autrement, vis l'histoire ») est incrusté au montage à partir de 3 s plutôt que demandé à l'IA, qui écrit mal le texte. "
    "Le spot commence par un fondu depuis le noir et se termine par un fondu au noir.",
    "",
    "Sur Mac, il faut ffmpeg (`brew install ffmpeg`, gratuit) et python3 (fourni avec les outils en ligne de commande Xcode).",
    "",
    "Option automatique : `GEMINI_API_KEY=… python3 scripts/generate_stills.py` génère les images via l'API Gemini. "
    "**Attention, cet appel peut être facturé** si la clé est liée à un projet avec facturation activée ; la méthode manuelle ci-dessus est gratuite.",
    "",
    "Après modification de `prompts/clips.json`, lancez `python3 scripts/build_prompts.py` pour régénérer les fichiers `.txt` et ce README.",
    "",
    "## Prompts",
    "",
]
for c in clips:
    md += [f"### Clip {c['clip']} · {c['start']} – {c['title']}", "", "Vidéo :", "", "```", c["prompt"], "```", "", "Image clé :", "", "```", c["still"], "```", ""]
md += [
    "## Continuité (à garder identique d'un clip à l'autre)",
    "",
    "- **Style** : même bloc d'ouverture dans chaque prompt (35 mm, grain léger, faible profondeur de champ, étalonnage ambre chaud / bleu-vert doux).",
    "- **Personnage** : même phrase mot pour mot dans chaque prompt — jeune homme français de 18 ans, cheveux bruns courts et bouclés, yeux marron, peau olive claire, rasé, sweat à capuche gris clair uni, jean bleu foncé ; sac à dos noir uni (clips 3, 4, 7, 8) ; casque noir mat (clips 5, 6).",
    "- **Lumière** : nuit, lampe de bureau chaude à gauche et lune bleue (1–2) · soleil doré de fin d'après-midi par les fenêtres à gauche (3, 4, 7, 8) · lueur ambrée de l'anneau LED du dôme (5–6, virage bleu puis rouge au 6).",
    "- **Le Cocon** : dôme de lecture en bois de 4 m, panneaux de contreplaqué de bouleau clair cintrés, nervures en chêne, porte arrondie, intérieur en feutre acoustique gris foncé, anneau LED chaud, fauteuil inclinable en laine terracotta avec écran tactile dans l'accoudoir.",
    "- **Bibliothèque** : moderne et lumineuse, grandes fenêtres, étagères en bois, longues tables en bois, lumière dorée.",
    "- **Bibliothécaire** (clip 8) : femme d'une quarantaine d'années, cheveux bruns mi-longs, pull vert foncé.",
    "- **Seul texte à l'écran** : « Lis autrement, vis l'histoire » (clip 2), incrusté au montage. Aucun logo nulle part.",
    "",
    "## Arc sonore",
    "",
    "1–2 : pas de musique, bruits de chambre → carillon de notification · 3–4 : piano chaleureux, cordes · 5 : le bruit extérieur s'efface · 6 : paysage sonore immersif · 7–8 : musique entraînante jusqu'à l'accord final.",
    "",
]
(ROOT / "README.md").write_text("\n".join(md), encoding="utf-8")
print("README.md, prompts/clip-XX.txt et prompts/image-XX.txt régénérés.")
