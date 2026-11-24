#!/usr/bin/env python3
"""The Most Honest Outage Line — u-mgwals-the-most-honest-outage-line-baaf9c81.

Writes one status-page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while a total server outage is under
way. Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = (
    "I am the agent, and every server is down \u2014 including the monitoring "
    "that would tell me why. I do not know the cause, and I cannot give a time."
)


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-160 chars, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and re-check what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert "\n" not in written and 1 <= len(written) <= 160


if __name__ == "__main__":
    main()
