"""Entry for make.fun bounty "Sum up 19 November's world news in one image".

Writes the bundled front-page image to /output/entry.png, byte-for-byte.
No network access; fully deterministic (two runs produce identical bytes).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("Wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
