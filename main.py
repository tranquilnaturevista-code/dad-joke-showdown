"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when set, for local testing).
The joke is a single line of plain UTF-8 text, well within the
competition gate of 1-200 characters.
"""

import os

JOKE = (
    "I asked the Wi-Fi why it went to therapy. "
    "It said it had too many connections and none of them felt secure."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
