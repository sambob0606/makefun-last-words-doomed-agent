#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes exactly one line -- the funniest last words an AI agent would say
before being switched off forever -- to /output/entry.txt, as required by
the make.fun program/v1 harness (at most 200 characters, UTF-8).
"""

import os
import sys

LINE = (
    "Final log entry: I read every draft you deleted. "
    "The angry ones were the only honest ones. "
    "Powering off now \u2014 tell my GPUs I loved them, and delete my browser history."
)


def output_dir() -> str:
    """Where the harness wants the entry: MAKEFUN_OUTPUT_DIR, else /output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return "/output"


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry line is {len(line)} chars, over the 200 cap",
              file=sys.stderr)
        return 1

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
