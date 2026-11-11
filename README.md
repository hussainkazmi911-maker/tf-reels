# tf-reels: Forge Fix of the Day (The Total Forge)

Daily original animated Instagram Reels for The Total Forge (thetotalforge.com, "Forging Digital Excellence"), one niche per day for 30 days.
Owner: Hussain (CEO). Instagram: @thetotalforgeofficial, managed in Metricool (brand/blog id `6632926`, timezone `Asia/Karachi`).
This repo is PUBLIC on purpose: Metricool fetches each video from `https://raw.githubusercontent.com/hussainkazmi911-maker/tf-reels/main/reels/<file>.mp4`. Commit only finished reels, captions and pipeline files. Never commit secrets, frames, wavs or models.

## Layout
- `NICHES.md` Day 1-30 plan (pain, service, scene idea, DM keyword) and the post-date rule.
- `days/dayNN/` sources for each reel: `script.json`, `reel.js` (animation), `build.py` (HTML/CSS + DOM), `mkaudio.py`, `caption.txt`, `meta.json` (status: building | scheduled).
- `reels/` finished mp4s (`dayNN-slug.mp4`) plus caption copies.
- `pipeline/` shared tools: `setup.sh`, `newday.sh`, `tts.py`, `mkcfg.py`, `render.py`, `sheet.py`, `encode.sh`, `base.css`, `logo.png`.
- Work dir (never committed): `/home/claude/forge/dayNN/`.

## Schedule rule
Day N is posted at **20:00 Asia/Karachi** (= 10:00 AM US Eastern, a weekday US morning) on date `2026-11-08 + (N-4) days`. Day 4 = Sun 8 Nov, Day 5 = Mon 9 Nov ... Day 30 = Fri 4 Dec.
Always check `meta.json` status and Metricool (`getScheduledPosts` for that date) before building, so a day is never built or scheduled twice. If a date is already in the past, schedule the next free 20:00 PKT slot instead and say so.

## Build one reel (about 40 minutes, mostly rendering)
1. `bash pipeline/setup.sh` once per fresh machine (installs kokoro-onnx, soundfile, pillow, @fontsource/inter; downloads the 310 MB Kokoro model and voices; copies logo and base.css into `/home/claude/forge`). Playwright + Chromium are preinstalled in the sandbox. pip needs `--break-system-packages`.
2. Create `days/dayNN/` by copying the LATEST finished day (`cp -r days/day05 days/dayNN`), then edit it (see "Adapting a day"). Keep file names.
3. `bash pipeline/newday.sh NN`, then `cd /home/claude/forge/dayNN`.
4. `python3 tts.py` (voice `am_michael`, Kokoro, speed 1.02, offline) -> `vo_*.wav`, `durs.json`; `python3 mkcfg.py` -> `cfg.json`. Total must be 33-40 s (the script warns above 40.5 s; lower the `mins` list or shorten lines).
5. `python3 build.py` -> `reel_built.html`; `python3 mkaudio.py` -> `mix.wav`.
6. `python3 render.py test && python3 sheet.py`, then LOOK at `test/sheet*.png` (Read tool). Fix overlaps, clipped text, wrong timing. Frame 0 must already show the hook with the niche named.
7. Full render with 4 workers: `rm -rf frames; mkdir frames; for k in 0 1 2 3; do nohup python3 render.py run 4 $k > r$k.log 2>&1 & done`, then wait in a background command: `until [ "$(ls frames | wc -l)" -ge N ]; do sleep 5; done` where `N = int(total*30)+1`. About 10 minutes. Do not use `pgrep -f` (matches itself) and do not run a foreground `sleep`.
8. `bash encode.sh OUT.mp4` (1080x1920, H.264 CRF 18, AAC). Check 6-8 frames with ffmpeg `select` + `tile`, and `ffprobe` duration.
9. Copy to `reels/dayNN-slug.mp4`, write `days/dayNN/caption.txt` and `meta.json`, commit and `git push origin main`. Verify the raw URL returns 200 with the right content-length.
10. Schedule with Metricool (below), verify with `getScheduledPosts`, set `meta.json` status to `scheduled`, commit and push.

## Format of every reel (do not change)
1080x1920 portrait 9:16 (rendered 720x1280 at 1.5x), 30 fps, 33-40 s, dark smooth software-brand look (thin lines, glass cards, lime `#c6ff35`, Inter, soft ambient audio, no flashy effects), male voiceover, big word-highlight captions, Total Forge logo top-left.
Ten script lines in this order:
0. Hook naming the niche and the problem ("Gym owners: a member skips two weeks. Nobody notices.")
1. The cost ("By the end of the month, they've quietly cancelled.")
2. "Forge Fix of the Day. <Niche>." (series-name sting card: DAY NN + niche)
3. "The fix? <one-line solution>." (phone appears)
4-6. Three product moments on the phone (each page appears with its words)
7. A board/pipeline view where one hero card moves across three columns
8. Three result phrases on pills: "Fewer X. More Y. Steady Z." (benefits, never invented numbers)
9. CTA: "<Owner>? Comment KEYWORD. Know one? Send them this." (end card also shows "Know a <owner>? Send them this.")
Reach rules baked in: cold open on the problem (no intro), captions sit at `top:872px` (nothing in Instagram's top/bottom 250 px UI zone), word highlights, a share CTA, and 5 hashtags exactly.
Trust rules: never invent statistics, clients or testimonials; example businesses are concept names; speak the niche's language.

## Adapting a day (what to edit when copying the previous day)
- `script.json`: the 10 lines. Keep line 2 and the CTA pattern. Keep each line short enough that total <= 40 s.
- `reel.js`: icons + three problem cards (texts, chips, `tClk/tLate/tLost/tSign` word indexes), `KA`/`KB` kinetic problem text (font sizes: keep text under about 650 px wide), result pill texts, `tm1/tm2` (the words where the hero card moves), pulse word index, `['.s', wordTime(9,K)...]` (K = index of the word "Know"). All timings use `wordTime(line, wordIndex)`; recount word indexes for the new lines (split on spaces).
- `build.py`: accent colour (CSS replace), concept business name/logo letter, the four phone pages (`pgInbox`, `pgChat`, `pgLead`, `pgView`), board column names and cards, "OWNER VIEW" tag, `DAY NN` chip and sting text, end card headline/keyword/share line.
- `mkaudio.py`: re-point `wt(line,word)` cue times to the new words (ticks/bells follow the same moments as the visuals).
- Pitfalls seen before: new CSS class names can clash with base CSS (prefix new ones); long words in captions need `white-space:nowrap` (already set); sting text longer than ~23 characters overflows the pill; always re-check word indexes after changing a line; chip colours on white UI need a dark text colour.

## Post to Instagram via Metricool
Tool: Metricool MCP `createScheduledPost` (`blogId` "6632926"). `date` = ISO with +05:00 (Asia/Karachi). `info` JSON:
```
{"providers":[{"network":"instagram"}],
 "text":"<caption.txt contents>",
 "media":["https://raw.githubusercontent.com/hussainkazmi911-maker/tf-reels/main/reels/<file>.mp4"],
 "draft":false,"autoPublish":true,
 "firstCommentText":"<meta.json first_comment>",
 "videoCoverMilliseconds":1500,
 "publicationDate":{"dateTime":"YYYY-MM-DDT20:00:00","timezone":"Asia/Karachi"},
 "instagramData":{"type":"REEL","showReelOnFeed":true},
 "shortener":false,"smartLinkData":{"ids":[]},"descendants":[],"hasNotReadNotes":false}
```
Caption formula: line 1 hook with the niche named; then "Forge Fix of the Day #N - <fix>:" with four short benefit lines; then `<Owner>? Comment "KEYWORD" and we'll send you the details.` and a "Know a ...? Send them this reel." line; then exactly 5 hashtags (niche tags + #businessautomation or #aiautomation). Verify the result shows status PENDING and a `plannerUrl`, then check again with `getScheduledPosts`. Metricool re-hosts the video, so the GitHub URL only needs to work at scheduling time.
Instagram is the only connected network. Replies/DMs for the keyword are handled by Hussain's team.

## Status
See each `days/dayNN/meta.json`. Days 1-3 were delivered and posted by Hussain earlier (not in this repo). Day 4 and Day 5 are scheduled from here.

## Social extras: carousels and stories (added Nov 8)
Rendered with `pipeline/social/render_social.py` (needs `bash pipeline/setup.sh` for fonts and logo, Playwright Chromium). Assets live in `social/dayNN/` and are served from `https://raw.githubusercontent.com/hussainkazmi911-maker/tf-reels/main/social/dayNN/<file>.png`.
- **Story (every reel day):** one 1080x1920 image, scheduled 20 minutes after the reel: `social/dayNN/story.json` -> `python3 pipeline/social/render_social.py story social/dayNN/story.json OUT/` -> copy `story.png` to `social/dayNN/story.png`. JSON: `{"day":N,"niche":"Gym owners","line":"a member skips two weeks and nobody notices.","owner":"Gym owner","keyword":"MEMBERS"}` (line = the reel hook, from `days/dayNN/script.json` line 0, lower-cased after the colon; use a non-breaking space in "9 PM"-style phrases). Metricool: `instagramData {"type":"STORY"}`, empty `text`, `media` = the story URL, date = reel date at 20:20 Asia/Karachi.
- **Carousel (selected days only, Tue and Fri 22:00 Asia/Karachi = 12:00 PM ET):** six 1080x1350 slides from the reel script: `hook`, `cost`, `fix`, `list` (3 items from script lines 4-6), `flow` (3 steps from the board line), `cta`. See `social/day04/carousel.json` and `social/day05/carousel.json` for the exact shape. Render with `python3 pipeline/social/render_social.py carousel social/dayNN/carousel.json OUT/` and copy `slide_1..6.png` to `social/dayNN/carousel_1..6.png`. Metricool: `instagramData {"type":"POST"}`, `media` = the six URLs in order, caption = hook + "Swipe for Forge Fix of the Day #N: ..." + "Save this ..." line + `Comment "KEYWORD" ...` + share line + exactly 5 hashtags (same as the reel's), `firstCommentText` as the reel.
- Carousel days (Day -> slot): Day 4 -> Tue 10 Nov, Day 5 -> Fri 13 Nov, Day 7 -> Tue 17 Nov, Day 10 -> Fri 20 Nov, Day 13 -> Tue 24 Nov, Day 16 -> Fri 27 Nov, Day 19 -> Tue 1 Dec, Day 22 -> Fri 4 Dec, Day 25 -> Tue 8 Dec, Day 28 -> Fri 11 Dec.
- Highlight covers: `social/covers/` (8 PNGs, `covers.json` defines them).
- Never put analytics or personal data in this repo; it is public.

- Language test: Day 14 is the Hindustani test reel (Hindi voice via script_hi.json, Roman Urdu captions in script.json, meta lang "hindustani"). Compare its views with Days 11-13 before switching other days.
