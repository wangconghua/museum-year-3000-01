#!/usr/bin/env python3
"""Museum of the Year 3000 -- entry.

Writes a single original museum label (year 3000, beside an ordinary
object from today: a pine-tree car air freshener) to /output/entry.txt
(or $ENTRY_OUTPUT).
"""

import os
import sys

LABEL = (
    "The last tree of the 21st century, preserved in scented plastic "
    "and hung from car mirrors so drivers could remember forests."
)

MAX_CHARS = 200


def check_single_line(text):
    """The label must be one line: no embedded line breaks."""
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    return True


def validate(text):
    """Check the label is UTF-8, 1-200 chars, and not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("label must be a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not text.strip():
        raise ValueError("label must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"label is {len(text)} chars, over the 200 limit")
    check_single_line(text)
    return True


def main():
    validate(LABEL)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # Deterministic: fixed bytes, single trailing newline, no timestamps.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
