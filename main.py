#!/usr/bin/env python3
"""The One-Line Laugh: writes a single funny line to entry.txt.

Stdlib only, no network, deterministic. The line is a single sentence of
at most 200 characters, checked before writing.
"""

import os
import sys

LINE = (
    "My fitness tracker congratulated me on 10,000 steps, "
    "every one of them pacing the kitchen trying to decide what to eat."
)


def main() -> int:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single sentence on one line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
