# Spot publicitaire « Le Cocon » — bibliothèque

Spot de 64 secondes, 8 clips de 8 s générés par IA vidéo (prompts en anglais, prêts à copier-coller).

| # | Début | Titre | Prompt | Rush attendu |
|---|---|---|---|---|
| 1 | 0:00 | La difficulté | [`prompts/clip-01.txt`](prompts/clip-01.txt) | `clips/clip-01.mp4` |
| 2 | 0:08 | La découverte | [`prompts/clip-02.txt`](prompts/clip-02.txt) | `clips/clip-02.mp4` |
| 3 | 0:16 | Arrivée en bibliothèque | [`prompts/clip-03.txt`](prompts/clip-03.txt) | `clips/clip-03.mp4` |
| 4 | 0:24 | Le Cocon | [`prompts/clip-04.txt`](prompts/clip-04.txt) | `clips/clip-04.mp4` |
| 5 | 0:32 | Il s'installe | [`prompts/clip-05.txt`](prompts/clip-05.txt) | `clips/clip-05.mp4` |
| 6 | 0:40 | L'immersion | [`prompts/clip-06.txt`](prompts/clip-06.txt) | `clips/clip-06.mp4` |
| 7 | 0:48 | La sortie | [`prompts/clip-07.txt`](prompts/clip-07.txt) | `clips/clip-07.mp4` |
| 8 | 0:56 | La carte de bibliothèque | [`prompts/clip-08.txt`](prompts/clip-08.txt) | `clips/clip-08.mp4` |

## Montage

1. Générez chaque clip avec son prompt et déposez le fichier dans `clips/` sous le nom `clip-01.mp4` … `clip-08.mp4`.
2. Lancez `./scripts/montage.sh`.
3. Le spot est écrit dans `output/spot-le-cocon.mp4` (1920×1080, 24 i/s, H.264 + AAC, 64 s).

Si un rush manque, le script le remplace par un carton (animatique) indiquant le numéro, le titre et le timecode du plan : on peut donc monter et vérifier le rythme avant d'avoir tous les clips. Chaque rush est recadré au format 16:9, ramené à 8 s exactement, et son son est normalisé (fondu de 0,15 s en entrée et en sortie pour éviter les clics aux coupes). Un rush sans piste audio reçoit un silence. Le spot commence par un fondu depuis le noir et se termine par un fondu au noir.

Après modification de `prompts/clips.json`, lancez `python3 scripts/build_prompts.py` pour régénérer les fichiers `.txt` et ce README.

## Prompts

### Clip 1 · 0:00 – La difficulté

```
Cinematic 8-second commercial shot, photorealistic, 35mm film look, shallow depth of field. A French 18-year-old young man with short curly brown hair and a light grey hoodie sits on his bed in a dim bedroom at night, lit only by a small warm desk lamp, cool blue shadows. Slow dolly-in toward him as he tries to read a paperback novel, frowning, bored and frustrated. At the end he sighs, snaps the book shut and reaches for his smartphone on the bed. Sound: quiet room tone, clock ticking, a page turning, a heavy sigh, the dull thud of the book closing. No music, no text, no subtitles, no logos.
```

### Clip 2 · 0:08 – La découverte

```
Cinematic 8-second commercial shot, photorealistic. First-person POV in a dark bedroom: a hand in a light grey hoodie sleeve holds a smartphone, the thumb scrolls a vertical short-video feed (generic interface, no brand logos), screen glow lights the fingers. The scrolling stops on a dynamic video showing a futuristic wooden dome reading pod (curved light birch plywood panels, oak ribs) with a terracotta wool armchair inside a bright modern library, with the white on-screen caption "Lis autrement, vis l'histoire". Slow push-in on the screen; the faint reflection of the young man's face (curly brown hair) appears on the glass and lights up with curiosity. Sound: soft swipe sounds, a gentle notification chime, a subtle rising tone.
```

### Clip 3 · 0:16 – Arrivée en bibliothèque

```
Cinematic 8-second commercial shot, photorealistic, warm golden daylight. Wide shot: the same French 18-year-old young man with short curly brown hair, light grey hoodie and black backpack walks into a bright modern public library with tall windows, wooden bookshelves and students studying at long wooden tables. He looks around and smiles. Smooth steadicam tracking shot following him. Warm, luminous, inviting color grade. Sound: soft library ambience, footsteps, a warm hopeful piano melody begins. No text, no logos.
```

### Clip 4 · 0:24 – Le Cocon

```
Cinematic 8-second commercial shot, photorealistic. Slow panoramic camera move revealing, in the lounge area of a bright modern library, a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs, its wide rounded door open, warm amber light glowing inside, a reclining terracotta wool armchair visible within. The young man with short curly brown hair and light grey hoodie, seen from behind at the edge of frame, stops and looks at it, fascinated. Golden daylight, premium Scandinavian design. Sound: warm piano and soft strings, gentle whoosh. No text, no logos.
```

### Clip 5 · 0:32 – Il s'installe

```
Cinematic 8-second commercial shot, photorealistic. Inside a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs, dark grey acoustic felt walls between the curved oak ribs, warm LED ring light in the ceiling. Medium shot: the young man with short curly brown hair and light grey hoodie sits down comfortably in a reclining terracotta wool armchair, puts on sleek over-ear headphones, taps a small touchscreen built into the armrest to choose a story, then closes his eyes with a slight smile as the light slowly dims. Sound: soft fabric movement, a subtle touchscreen click, the outside noise fades into silence. No text, no logos, no readable text on the touchscreen or headphones.
```

### Clip 6 · 0:40 – L'immersion

```
Cinematic 8-second commercial shot, photorealistic with subtle visual effects. Inside a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs, dark grey acoustic felt walls, the young man with short curly brown hair and a light grey hoodie wears over-ear headphones, eyes closed, reclining in a terracotta armchair, completely immersed and peaceful. The interior light slowly shifts from cold blue to warm deep red, soft haze, light particles drifting, a gentle breeze moves his hair, the armchair vibrates very slightly. Slow orbiting camera around his face. Sound: deep immersive soundscape, low rumble, wind, distant heartbeat, ethereal music. No text, no logos.
```

### Clip 7 · 0:48 – La sortie

```
Cinematic 8-second commercial shot, photorealistic, warm daylight. The young man with short curly brown hair, light grey hoodie and black backpack steps out of the wide open rounded door of a 4-meter wooden dome reading pod made of curved light birch plywood panels with oak ribs in a bright modern library. He looks rested, focused and genuinely enthusiastic, takes a deep breath and grins. Medium shot, slight handheld feel. Sound: uplifting warm music builds, door creak, soft library ambience. No text, no logos.
```

### Clip 8 · 0:56 – La carte de bibliothèque

```
Cinematic 8-second commercial shot, photorealistic. At the wooden reception desk of a bright modern public library, a friendly female librarian in her forties with shoulder-length brown hair and a dark green sweater hands a library membership card to the young man with short curly brown hair, light grey hoodie and black backpack. He takes it with a big smile. Warm golden light, bookshelves in the background, final hero shot, slow push-in. Sound: uplifting music reaches its final chord. No readable text on the card, no logos.
```

## Continuité (à garder identique d'un clip à l'autre)

- **Personnage** : jeune homme français de 18 ans, cheveux bruns courts et bouclés, sweat à capuche gris clair, sac à dos noir (clips 3, 7, 8).
- **Le Cocon** : dôme de lecture en bois de 4 m, panneaux de contreplaqué de bouleau clair cintrés, nervures en chêne, porte arrondie, intérieur en feutre acoustique gris foncé, anneau LED chaud, fauteuil inclinable en laine terracotta avec écran tactile dans l'accoudoir.
- **Bibliothèque** : moderne et lumineuse, grandes fenêtres, étagères en bois, longues tables en bois, lumière dorée.
- **Bibliothécaire** (clip 8) : femme d'une quarantaine d'années, cheveux bruns mi-longs, pull vert foncé.
- **Seul texte à l'écran** : « Lis autrement, vis l'histoire » (clip 2). Aucun logo nulle part.

## Arc sonore

1–2 : pas de musique, bruits de chambre → carillon de notification · 3–4 : piano chaleureux, cordes · 5 : le bruit extérieur s'efface · 6 : paysage sonore immersif · 7–8 : musique entraînante jusqu'à l'accord final.
