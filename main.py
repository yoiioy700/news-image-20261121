"""Put the finished front page where the competition expects it.

The broadsheet lives in this repository as frontpage.png. This script
reads it, makes sure it is a whole PNG of the right shape, and writes
an identical copy called entry.png into the output directory. It only
uses the Python standard library and never touches the network.
"""

import os
import sys
from hashlib import sha256

SIGNATURE = b"\x89PNG\r\n\x1a\n"
PAGE_FILE = "frontpage.png"
ENTRY_FILE = "entry.png"
MAX_BYTES = 1048576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def check_limits(content, width, height):
    if len(content) > MAX_BYTES:
        sys.exit("page too large: " + str(len(content)) + " bytes, "
                 + "limit is " + str(MAX_BYTES))
    if width != EXPECTED_WIDTH or height != EXPECTED_HEIGHT:
        sys.exit("wrong page size: " + str(width) + "x" + str(height)
                 + ", expected " + str(EXPECTED_WIDTH) + "x"
                 + str(EXPECTED_HEIGHT))


def page_path():
    folder = os.path.dirname(os.path.abspath(__file__))
    found = os.path.join(folder, PAGE_FILE)
    if not os.path.isfile(found):
        sys.exit("front page not found beside this script: " + found)
    return found


def output_path():
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(chosen, exist_ok=True)
    return os.path.join(chosen, ENTRY_FILE)


def png_dimensions(content):
    if len(content) < 8 or content[:8] != SIGNATURE:
        sys.exit("not a PNG: the first bytes are not the PNG signature")
    if content[12:16] != b"IHDR":
        sys.exit("not a well-formed PNG: no IHDR chunk after the signature")
    if b"IEND" not in content[-16:]:
        sys.exit("PNG looks truncated: no IEND trailer at the end")
    width = int.from_bytes(content[16:20], "big")
    height = int.from_bytes(content[20:24], "big")
    return width, height


def main():
    source = page_path()
    with open(source, "rb") as handle:
        content = handle.read()
    width, height = png_dimensions(content)
    check_limits(content, width, height)
    target = output_path()
    with open(target, "wb") as handle:
        handle.write(content)
    with open(target, "rb") as handle:
        written = handle.read()
    if sha256(written).digest() != sha256(content).digest():
        sys.exit("copy check failed: " + target + " differs from " + source)
    print("wrote " + target + " (" + str(width) + "x" + str(height) + ", "
          + str(len(content)) + " bytes, sha256 "
          + sha256(content).hexdigest() + ")")


if __name__ == "__main__":
    main()
