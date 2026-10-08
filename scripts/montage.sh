#!/usr/bin/env bash
# Monte le spot à partir de clips/clip-01.mp4 … clip-08.mp4.
# Un rush manquant est remplacé par un carton d'animatique.
set -euo pipefail
shopt -s inherit_errexit 2>/dev/null || true

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLIPS="$ROOT/clips"
OUT="$ROOT/output"
WORK="$OUT/.work"
FONT="${FONT:-/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf}"
W=1920 H=1080 FPS=24 DUR=8 AF=0.15 TOTAL=64

mkdir -p "$WORK"
rm -f "$WORK"/*.mp4 "$WORK"/*.txt

# Titres et timecodes lus depuis prompts/clips.json (une ligne « n|start|title »).
mapfile -t META < <(python3 -c '
import json,sys
for c in json.load(open(sys.argv[1], encoding="utf-8")):
    print("%02d|%s|%s" % (c["clip"], c["start"], c["title"]))
' "$ROOT/prompts/clips.json")

for line in "${META[@]}"; do
  IFS='|' read -r n start title <<<"$line"
  src="$CLIPS/clip-$n.mp4"
  dst="$WORK/clip-$n.mp4"
  if [[ -f "$src" ]]; then
    echo "Clip $n : rush $src"
    has_audio=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$src" | head -1)
    vf="scale=$W:$H:force_original_aspect_ratio=increase,crop=$W:$H,setsar=1,fps=$FPS,tpad=stop_mode=clone:stop_duration=$DUR,trim=duration=$DUR,setpts=PTS-STARTPTS,format=yuv420p"
    if [[ -n "$has_audio" ]]; then
      ffmpeg -v error -y -i "$src" \
        -filter_complex "[0:v]$vf[v];[0:a]aresample=48000,aformat=channel_layouts=stereo,apad,atrim=duration=$DUR,afade=t=in:d=$AF,afade=t=out:st=$(echo "$DUR-$AF"|bc):d=$AF,asetpts=PTS-STARTPTS[a]" \
        -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k -ar 48000 "$dst"
    else
      ffmpeg -v error -y -i "$src" -f lavfi -t $DUR -i anullsrc=r=48000:cl=stereo \
        -filter_complex "[0:v]$vf[v]" -map "[v]" -map 1:a \
        -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k -ar 48000 -t $DUR "$dst"
    fi
  else
    echo "Clip $n : rush absent → carton d'animatique"
    # Textes passés par fichier pour ne pas avoir à échapper « ' », « : » ou « % ».
    printf '%s' "PLAN $((10#$n)) · $start" > "$WORK/t1.txt"
    printf '%s' "$title" > "$WORK/t2.txt"
    printf '%s' "rush attendu : clips/clip-$n.mp4" > "$WORK/t3.txt"
    ffmpeg -v error -y -f lavfi -i "color=c=0x1b1f24:s=${W}x${H}:r=$FPS:d=$DUR" -f lavfi -t $DUR -i anullsrc=r=48000:cl=stereo \
      -vf "drawtext=fontfile=$FONT:textfile=$WORK/t1.txt:fontcolor=0xd9a066:fontsize=46:x=(w-tw)/2:y=h/2-130,\
drawtext=fontfile=$FONT:textfile=$WORK/t2.txt:fontcolor=white:fontsize=96:x=(w-tw)/2:y=h/2-40,\
drawtext=fontfile=$FONT:textfile=$WORK/t3.txt:fontcolor=0x8a939c:fontsize=34:x=(w-tw)/2:y=h/2+110,format=yuv420p" \
      -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k -ar 48000 -t $DUR "$dst"
  fi
  echo "file '$dst'" >> "$WORK/list.txt"
done

# Assemblage en coupes franches, fondu depuis le noir au début et vers le noir à la fin.
ffmpeg -v error -y -f concat -safe 0 -i "$WORK/list.txt" \
  -vf "fade=t=in:d=0.5,fade=t=out:st=$((TOTAL-1)):d=1" -af "afade=t=in:d=0.5,afade=t=out:st=$((TOTAL-1)):d=1" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
  "$OUT/spot-le-cocon.mp4"

echo "Spot monté : $OUT/spot-le-cocon.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/spot-le-cocon.mp4") s)"
