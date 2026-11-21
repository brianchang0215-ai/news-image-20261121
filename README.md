# Sum up 21 November's world news in one image

Entry for the make.fun bounty
[“Sum up 21 November's world news in one image”](https://make.fun/bounty/news-image-20261121)
($100, ends 2026-11-23 00:00 UTC / 08:00 Taipei).

## What it is

One image summarising Saturday 21 November 2026, in four panels:

1. **Russia strikes Ukraine** — 400+ drones, 110 missiles; missiles land in Poland.
2. **AI stocks tumble** — S&P 500 enters correction, down 3.7%.
3. **ICJ: Myanmar guilty of genocide** — first state held responsible over the Rohingya.
4. **Cancer pill breakthrough** — tumours undetectable in 1 in 12 patients.

The image is a whole PNG, 1024 × 1024 pixels, 718,691 bytes
(under the 1 MiB limit). It is held in this repository as base64 text
at `assets/entry.png.b64`; `main.py` decodes it to reproduce the PNG
byte for byte. (A plain `assets/entry.png`, if present, is copied
directly instead.)

## How to run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) writes
the image to `output/entry.png` (and also tries the absolute
`/output/entry.png` when that directory exists). Running it twice
writes the same bytes both times — verified locally with `sha256sum`.

## Verification (local, 2026-11-21)

```sh
python3 main.py
sha256sum output/entry.png
python3 main.py
sha256sum output/entry.png   # identical hash
python3 -c "from PIL import Image; im = Image.open('output/entry.png'); print(im.format, im.size)"
# PNG (1024, 1024)
```

## Notes for submission

- This repository is the public entry repository for the bounty;
  submitting it to make.fun is a separate step, not yet done.
- The bounty brief also asks for the AI coding-agent transcripts of
  the sessions that built the entry, uploaded with each submission.
  Those transcripts are **not** included here; they must be reviewed
  (and checked for personal information) before anything is uploaded.
- No wallet address, private key, recovery phrase, or personal
  information is included in this repository.
- At most 10 submissions a day and 20 in all; the last submission
  before the deadline is the final entry.
