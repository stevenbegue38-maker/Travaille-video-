# Spot publicitaire « Le Cocon » — bibliothèque

Spot de 64 secondes, 8 clips de 8 s générés par IA vidéo (prompts en anglais, prêts à copier-coller).

| # | Début | Titre | Ce soir | Prompt vidéo | Prompt image | Fichier à déposer |
|---|---|---|---|---|---|---|
| 1 | 0:00 | La difficulté | vidéo Flow | [`clip-01.txt`](prompts/clip-01.txt) | [`image-01.txt`](prompts/image-01.txt) | `clips/clip-01.mp4` |
| 2 | 0:08 | La découverte | image animée | [`clip-02.txt`](prompts/clip-02.txt) | [`image-02.txt`](prompts/image-02.txt) | `stills/clip-02.png` |
| 3 | 0:16 | Arrivée en bibliothèque | vidéo Flow | [`clip-03.txt`](prompts/clip-03.txt) | [`image-03.txt`](prompts/image-03.txt) | `clips/clip-03.mp4` |
| 4 | 0:24 | Le Cocon | image animée | [`clip-04.txt`](prompts/clip-04.txt) | [`image-04.txt`](prompts/image-04.txt) | `stills/clip-04.png` |
| 5 | 0:32 | Il s'installe | vidéo Flow | [`clip-05.txt`](prompts/clip-05.txt) | [`image-05.txt`](prompts/image-05.txt) | `clips/clip-05.mp4` |
| 6 | 0:40 | L'immersion | image animée | [`clip-06.txt`](prompts/clip-06.txt) | [`image-06.txt`](prompts/image-06.txt) | `stills/clip-06.png` |
| 7 | 0:48 | La sortie | vidéo Flow | [`clip-07.txt`](prompts/clip-07.txt) | [`image-07.txt`](prompts/image-07.txt) | `clips/clip-07.mp4` |
| 8 | 0:56 | La carte de bibliothèque | vidéo Flow | [`clip-08.txt`](prompts/clip-08.txt) | [`image-08.txt`](prompts/image-08.txt) | `clips/clip-08.mp4` |

## Tout faire en une soirée, gratuitement

Google Flow gratuit donne environ 50 crédits par jour et un clip Veo 3.1 Lite en coûte 10 : 5 vidéos par soir. Les plans 1, 3, 5, 7, 8 (ceux qui ont le plus d'action) sont donc faits en vidéo, les plans 2, 4, 6 en image fixe animée par un zoom lent au montage.

**Règle d'or : aucun abonnement, aucune carte bancaire.** Si une page demande un paiement, on s'arrête.

1. **Personnage de référence** (app Gemini gratuite, gemini.google.com) : collez [`prompts/reference-personnage.txt`](prompts/reference-personnage.txt), gardez l'image dont le visage vous plaît.
2. **Les 8 images clés** (app Gemini) : pour chaque plan, joignez l'image de référence et collez « Keep exactly the same young man as in the attached image (face, hair, clothes). » suivi du contenu de `prompts/image-XX.txt`. Enregistrez les images des plans 2, 4, 6 sous `stills/clip-XX.png` (les autres servent de première image à Flow).
3. **Les vidéos** (labs.google/flow, compte Google personnel) : vérifiez le solde (~50 crédits) sous la photo de profil, choisissez **Veo 3.1 Lite**, format 16:9, 8 s. Pour chacun des plans 1, 3, 5, 7, 8 : mode « Frames to Video » avec l'image clé du plan en première image, collez `prompts/clip-XX.txt`, générez **une seule fois**, téléchargez sous `clips/clip-XX.mp4`. Si le solde ne suffit plus, le plan restant passe en image animée (déposez simplement `stills/clip-XX.png`).
4. **Montage** : `./scripts/montage.sh` → `output/spot-le-cocon.mp4` (1920×1080, 24 i/s, H.264 + AAC, 64 s).

Usage commercial : les conditions de Google pour l'offre gratuite de Flow ne le confirment pas clairement, et un filigrane visible peut être ajouté selon le pays. Vérifiez avant toute diffusion payante.

## Montage

Pour chaque plan, le script prend la vidéo `clips/clip-XX.mp4`, sinon l'image `stills/clip-XX.png` (zoom lent de 8 s), sinon un carton d'animatique indiquant le numéro, le titre et le timecode du plan : on peut monter et vérifier le rythme avant d'avoir tous les clips. Chaque rush est recadré au format 16:9, ramené à 8 s exactement, et son son est normalisé (fondu de 0,15 s en entrée et en sortie). Un rush sans piste audio reçoit un silence. Le sous-titre « caption » d'un plan (clip 2 : « Lis autrement, vis l'histoire ») est incrusté au montage à partir de 3 s plutôt que demandé à l'IA, qui écrit mal le texte. Le spot commence par un fondu depuis le noir et se termine par un fondu au noir.

Sur Mac, il faut ffmpeg (`brew install ffmpeg`, gratuit) et python3 (fourni avec les outils en ligne de commande Xcode).

Option automatique : `GEMINI_API_KEY=… python3 scripts/generate_stills.py` génère les images via l'API Gemini. **Attention, cet appel peut être facturé** si la clé est liée à un projet avec facturation activée ; la méthode manuelle ci-dessus est gratuite.

Après modification de `prompts/clips.json`, lancez `python3 scripts/build_prompts.py` pour régénérer les fichiers `.txt` et ce README.

## Prompts

### Clip 1 · 0:00 – La difficulté

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans sits on his bed in a dim bedroom, trying to read a paperback novel, frowning, bored and frustrated. At the end he sighs, snaps the book shut and reaches for his smartphone on the bed. Camera: slow dolly-in toward him. Lighting: night, a single small warm desk lamp as key light from the left, cool blue moonlight fill from the window, deep soft shadows. Sound: quiet room tone, clock ticking, a page turning, a heavy sigh, the dull thud of the book closing, no music. No text, no subtitles, no logos.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans sits on his bed in a dim bedroom, trying to read a paperback novel, frowning, bored and frustrated. At the end he sighs, snaps the book shut and reaches for his smartphone on the bed. Framing: slow dolly-in toward him. Lighting: night, a single small warm desk lamp as key light from the left, cool blue moonlight fill from the window, deep soft shadows. No text, no subtitles, no logos.
```

### Clip 2 · 0:08 – La découverte

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Scene: first-person POV in the same dark bedroom, a hand in a light grey hoodie sleeve holds a smartphone; the thumb scrolls a vertical short-video feed (generic interface) and stops on a video showing a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs and a wide rounded doorway, a terracotta wool armchair inside, in a bright modern public library with tall windows, light wooden bookshelves and long wooden tables. The screen glow lights the fingers; the faint reflection of the young man's face with short curly brown hair appears on the glass, lighting up with curiosity. Camera: slow push-in on the screen. Lighting: night, a single small warm desk lamp as key light from the left, cool blue moonlight fill from the window, deep soft shadows. Sound: soft swipe sounds, a gentle notification chime, a subtle rising tone. No text, no subtitles, no logos. No readable text on screens, cards or headphones.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Scene: first-person POV in the same dark bedroom, a hand in a light grey hoodie sleeve holds a smartphone; the thumb scrolls a vertical short-video feed (generic interface) and stops on a video showing a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs and a wide rounded doorway, a terracotta wool armchair inside, in a bright modern public library with tall windows, light wooden bookshelves and long wooden tables. The screen glow lights the fingers; the faint reflection of the young man's face with short curly brown hair appears on the glass, lighting up with curiosity. Framing: slow push-in on the screen. Lighting: night, a single small warm desk lamp as key light from the left, cool blue moonlight fill from the window, deep soft shadows. No text, no subtitles, no logos. No readable text on screens, cards or headphones.
```

### Clip 3 · 0:16 – Arrivée en bibliothèque

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack, walks into a bright modern public library with tall windows, light wooden bookshelves and long wooden tables, students studying at the tables. He looks around and smiles. Camera: wide shot, smooth steadicam tracking shot following him. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. Sound: soft library ambience, footsteps, a warm hopeful piano melody begins. No text, no subtitles, no logos.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack, walks into a bright modern public library with tall windows, light wooden bookshelves and long wooden tables, students studying at the tables. He looks around and smiles. Framing: wide shot, smooth steadicam tracking shot following him. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. No text, no subtitles, no logos.
```

### Clip 4 · 0:24 – Le Cocon

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Scene: in the lounge area of a bright modern public library with tall windows, light wooden bookshelves and long wooden tables stands a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs and a wide rounded doorway, its door open, warm amber light glowing inside, a reclining terracotta wool armchair visible within. a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack, seen from behind at the edge of frame, stops and looks at it, fascinated. Premium Scandinavian design. Camera: slow panoramic move revealing the pod. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. Sound: warm piano and soft strings, a gentle whoosh. No text, no subtitles, no logos.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Scene: in the lounge area of a bright modern public library with tall windows, light wooden bookshelves and long wooden tables stands a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs and a wide rounded doorway, its door open, warm amber light glowing inside, a reclining terracotta wool armchair visible within. a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack, seen from behind at the edge of frame, stops and looks at it, fascinated. Premium Scandinavian design. Framing: slow panoramic move revealing the pod. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. No text, no subtitles, no logos.
```

### Clip 5 · 0:32 – Il s'installe

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Inside the 4-meter wooden dome reading pod: curved light birch plywood panels with oak ribs, dark grey acoustic felt between the ribs, a warm LED ring light in the ceiling, a reclining terracotta wool armchair with a small touchscreen in the armrest. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans sits down comfortably in the armchair, puts on sleek matte black over-ear headphones, taps the armrest touchscreen to choose a story, then closes his eyes with a slight smile as the light slowly dims. Camera: medium shot, static, slight push-in. Lighting: warm amber glow from the LED ring in the dome ceiling, soft and intimate. Sound: soft fabric movement, a subtle touchscreen click, the outside noise fades into silence. No text, no subtitles, no logos. No readable text on screens, cards or headphones.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Inside the 4-meter wooden dome reading pod: curved light birch plywood panels with oak ribs, dark grey acoustic felt between the ribs, a warm LED ring light in the ceiling, a reclining terracotta wool armchair with a small touchscreen in the armrest. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans sits down comfortably in the armchair, puts on sleek matte black over-ear headphones, taps the armrest touchscreen to choose a story, then closes his eyes with a slight smile as the light slowly dims. Framing: medium shot, static, slight push-in. Lighting: warm amber glow from the LED ring in the dome ceiling, soft and intimate. No text, no subtitles, no logos. No readable text on screens, cards or headphones.
```

### Clip 6 · 0:40 – L'immersion

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Inside the 4-meter wooden dome reading pod: curved light birch plywood panels with oak ribs, dark grey acoustic felt between the ribs, a warm LED ring light in the ceiling, a reclining terracotta wool armchair with a small touchscreen in the armrest. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans reclines in the armchair wearing sleek matte black over-ear headphones, eyes closed, completely immersed and peaceful. The interior light slowly shifts from cold blue to warm deep red, soft haze, light particles drifting, a gentle breeze moves his hair. Camera: slow orbit around his face, close-up. Lighting: starts from the warm amber LED ring glow, then shifts to cold blue and finally deep warm red, subtle visual effects. Sound: deep immersive soundscape, low rumble, wind, distant heartbeat, ethereal music. No text, no subtitles, no logos.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Inside the 4-meter wooden dome reading pod: curved light birch plywood panels with oak ribs, dark grey acoustic felt between the ribs, a warm LED ring light in the ceiling, a reclining terracotta wool armchair with a small touchscreen in the armrest. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans reclines in the armchair wearing sleek matte black over-ear headphones, eyes closed, completely immersed and peaceful. The interior light slowly shifts from cold blue to warm deep red, soft haze, light particles drifting, a gentle breeze moves his hair. Framing: slow orbit around his face, close-up. Lighting: starts from the warm amber LED ring glow, then shifts to cold blue and finally deep warm red, subtle visual effects. No text, no subtitles, no logos.
```

### Clip 7 · 0:48 – La sortie

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack, steps out of the wide rounded doorway of a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs and a wide rounded doorway in a bright modern public library with tall windows, light wooden bookshelves and long wooden tables. He looks rested, focused and genuinely enthusiastic, takes a deep breath and grins. Camera: medium shot, slight handheld feel. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. Sound: uplifting warm music builds, a soft wooden door creak, library ambience. No text, no subtitles, no logos.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Scene: a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack, steps out of the wide rounded doorway of a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs and a wide rounded doorway in a bright modern public library with tall windows, light wooden bookshelves and long wooden tables. He looks rested, focused and genuinely enthusiastic, takes a deep breath and grins. Framing: medium shot, slight handheld feel. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. No text, no subtitles, no logos.
```

### Clip 8 · 0:56 – La carte de bibliothèque

Vidéo :

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9. Scene: at the wooden reception desk of a bright modern public library with tall windows, light wooden bookshelves and long wooden tables, a friendly female librarian in her forties with shoulder-length brown hair and a dark green sweater hands a blank library membership card to a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack. He takes it with a big smile. Final hero shot. Camera: slow push-in. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. Sound: uplifting music reaches its final chord. No text, no subtitles, no logos. No readable text on screens, cards or headphones.
```

Image clé :

```
Single cinematic film still, key frame of a commercial, photorealistic, 35mm film look, soft film grain, shallow depth of field, warm amber and soft teal color grade, 16:9 landscape. Scene: at the wooden reception desk of a bright modern public library with tall windows, light wooden bookshelves and long wooden tables, a friendly female librarian in her forties with shoulder-length brown hair and a dark green sweater hands a blank library membership card to a French 18-year-old young man with short curly brown hair, brown eyes, light olive skin, clean-shaven, wearing a plain light grey hoodie with no print and dark blue jeans, with a plain black backpack. He takes it with a big smile. Final hero shot. Framing: slow push-in. Lighting: late-afternoon golden sunlight streaming through the tall windows from the left, soft warm bounce light, light haze. No text, no subtitles, no logos. No readable text on screens, cards or headphones.
```

## Continuité (à garder identique d'un clip à l'autre)

- **Style** : même bloc d'ouverture dans chaque prompt (35 mm, grain léger, faible profondeur de champ, étalonnage ambre chaud / bleu-vert doux).
- **Personnage** : même phrase mot pour mot dans chaque prompt — jeune homme français de 18 ans, cheveux bruns courts et bouclés, yeux marron, peau olive claire, rasé, sweat à capuche gris clair uni, jean bleu foncé ; sac à dos noir uni (clips 3, 4, 7, 8) ; casque noir mat (clips 5, 6).
- **Lumière** : nuit, lampe de bureau chaude à gauche et lune bleue (1–2) · soleil doré de fin d'après-midi par les fenêtres à gauche (3, 4, 7, 8) · lueur ambrée de l'anneau LED du dôme (5–6, virage bleu puis rouge au 6).
- **Le Cocon** : dôme de lecture en bois de 4 m, panneaux de contreplaqué de bouleau clair cintrés, nervures en chêne, porte arrondie, intérieur en feutre acoustique gris foncé, anneau LED chaud, fauteuil inclinable en laine terracotta avec écran tactile dans l'accoudoir.
- **Bibliothèque** : moderne et lumineuse, grandes fenêtres, étagères en bois, longues tables en bois, lumière dorée.
- **Bibliothécaire** (clip 8) : femme d'une quarantaine d'années, cheveux bruns mi-longs, pull vert foncé.
- **Seul texte à l'écran** : « Lis autrement, vis l'histoire » (clip 2), incrusté au montage. Aucun logo nulle part.

## Arc sonore

1–2 : pas de musique, bruits de chambre → carillon de notification · 3–4 : piano chaleureux, cordes · 5 : le bruit extérieur s'efface · 6 : paysage sonore immersif · 7–8 : musique entraînante jusqu'à l'accord final.
