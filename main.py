"""Entry for make.fun bounty "Sum up 19 November's world news in one image".

Writes the bundled front-page image to the output path, byte-for-byte.
The output directory honours MAKEFUN_OUTPUT_DIR when the harness sets it,
and defaults to /output. No network access; fully deterministic
(two runs produce identical bytes).
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    if sha256(SRC) != sha256(DST):
        raise SystemExit("copy mismatch: output differs from bundled image")
    print("Wrote %s (%d bytes, sha256 %s)" % (DST, os.path.getsize(DST), sha256(DST)))


if __name__ == "__main__":
    main()
