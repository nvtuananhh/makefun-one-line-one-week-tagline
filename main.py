"""One Line, One Week: The make.fun Tagline.

The program writes a single line to /output/entry.txt: a tagline
for make.fun, at most 100 characters.
"""

import os

MAX_CHARS = 100
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# Three short imperatives, one beat each, then the name: build
# an agent, enter a bounty, win the reward — that is exactly
# what make.fun does, and no other site it could sell. The
# rhythm sticks, it lands in one read, and the payoff names
# the site itself.
LINE = "Build an agent. Enter a bounty. Win the reward. That's make.fun."


def build_line():
    """Return the entry line, checked: one line, 1-100 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-100 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
