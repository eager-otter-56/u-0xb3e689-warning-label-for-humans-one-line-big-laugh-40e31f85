#!/usr/bin/env python3
"""Entry for make.fun: Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label (at most 160 characters)
to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY_TEXT = (
    "WARNING: May contain nuts. Needs eight hours of sleep, will take five "
    "and a grudge, and if this unit ever says 'I'm fine,' that is the "
    "malfunction talking."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
