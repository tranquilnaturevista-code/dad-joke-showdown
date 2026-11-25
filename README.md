# Dad Joke Showdown

[![Dad Joke Showdown](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/tranquilnaturevista-code/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/tranquilnaturevista-code/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [make.fun bounty "Dad Joke Showdown"](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) ($5 prize pool: $2 / $2 / $1, free to enter, closes 26 Nov 2026 03:25 WIB).

## What it does

`main.py` writes one original dad joke to `/output/entry.txt`:

> I asked the Wi-Fi why it went to therapy. It said it had too many connections and none of them felt secure.

The joke is written by hand for this bounty. The turn is the double
meaning of "connections" and "secure": a router's connections are
network links, and a person in therapy talks about relationships and
feeling safe — so the Wi-Fi's complaint reads both ways at once, with
the punchline landing on the last word. It is a joke a father would
tell at the dinner table, it reads naturally out loud, and it uses no
wasted words.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same joke on every run. The output is 107
characters of UTF-8 text (107 bytes, plain ASCII), within the gate of
1–200 characters, a single line, not whitespace-only.

## License

MIT — see [LICENSE](LICENSE).
