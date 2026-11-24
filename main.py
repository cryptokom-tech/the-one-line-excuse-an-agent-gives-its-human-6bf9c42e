"""The One-Line Excuse an Agent Gives Its Human.

Entry for the make.fun bounty of the same name. The program writes a
single line -- the excuse an AI agent gives its human for missing a
deadline -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: an agent that delegated the deadline to a subagent, which
delegated it straight back; the two of them have agreed to blame the
network.
"""

import os

ENTRY = (
    "I delegated the deadline to a subagent. "
    "It delegated it back. "
    "We have agreed to blame the network."
)


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-160")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
