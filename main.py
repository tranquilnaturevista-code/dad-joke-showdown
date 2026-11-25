"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when set, for local testing).
The joke is a single line of plain UTF-8 text, well within the
competition gate of 1-200 characters.
"""

import os

MAX_CHARS = 200  # competition gate: entry must be 1-200 characters


def validate(joke: str) -> str:
    """Return the joke unchanged, or fail loudly if it breaks the gate.

    The server rejects entries outside 1-200 characters or spanning
    more than one line, so check here instead of writing bad output.
    """
    text = joke.strip()
    if not text:
        raise SystemExit("error: joke is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"error: joke is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text:
        raise SystemExit("error: joke must be a single line")
    return text


JOKE = (
    "I asked the Wi-Fi why it went to therapy. "
    "It said it had too many connections and none of them felt secure."
)


def main() -> None:
    joke = validate(JOKE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"Wrote {len(joke)} characters to {path}")


if __name__ == "__main__":
    main()
