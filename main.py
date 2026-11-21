#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Sum up 21 November's world news in one image".

The program writes the image held in this repository to the output
location. Standard library only, no network, fully deterministic --
every run writes the same bytes.

The image is held as base64 text in ``assets/entry.png.b64`` so the
repository contains only text files; decoding it reproduces the PNG
byte for byte. If a plain ``assets/entry.png`` is present instead,
it is copied directly.
"""

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_PNG = ROOT / "assets" / "entry.png"
SOURCE_B64 = ROOT / "assets" / "entry.png.b64"


def load_image_bytes() -> bytes:
    if SOURCE_PNG.is_file():
        return SOURCE_PNG.read_bytes()
    if SOURCE_B64.is_file():
        return base64.b64decode(SOURCE_B64.read_text(encoding="ascii"))
    print(f"missing source image: {SOURCE_PNG} or {SOURCE_B64}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    data = load_image_bytes()

    destinations = [ROOT / "output" / "entry.png"]

    # The brief names the output "/output/entry.png". Also try that
    # absolute location when it exists and is writable, so the entry
    # works whether the harness mounts /output or runs in the repo.
    absolute_output = Path("/output/entry.png")
    if absolute_output.parent.is_dir():
        destinations.append(absolute_output)

    wrote_any = False
    for destination in destinations:
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            wrote_any = True
        except OSError as exc:
            print(f"could not write {destination}: {exc}", file=sys.stderr)

    if not wrote_any:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
