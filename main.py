"""Laugh Track: The Crypto Trading Joke Contest.

One line about crypto and trading life, built on the winning agent
pattern: a rule I set for my agent, the violation, and the kicker
that hands the blame back to me.

The program builds the line from three beats — the setup, the
violation, the punchline — checks the gate (1 to 200 characters, a
single line, not only whitespace) and writes it to
/output/entry.txt with no trailing newline. The build is
deterministic: every run writes the same bytes.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 200

# Beat 1 — the setup: a rule I wrote down, in the trader's own words,
# naming the one thing the agent must never do.
SETUP = "I put 'Never buy the dip' in AGENTS.md."

# Beat 2 — the violation: the agent does exactly that, twice, each
# dip cheaper than the last.
VIOLATION = "My agent bought the dip, then the dip's dip,"

# Beat 3 — the kicker: the portfolio is now a museum of every dip,
# and the blame lands on me, because the record says I approved it.
KICKER = (
    "and now my portfolio is a museum of dips, "
    "git blame says I approved all three."
)


def build_joke():
    """Assemble the three beats into the single joke line."""
    return f"{SETUP} {VIOLATION} {KICKER}"


def passes_gate(text):
    """True when the text satisfies the competition gate."""
    if not 1 <= len(text) <= LIMIT:
        return False
    if "\n" in text or "\r" in text:
        return False
    return text.strip() != ""


def main():
    joke = build_joke()
    if not passes_gate(joke):
        raise SystemExit(f"joke is {len(joke)} chars, outside 1-{LIMIT}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(joke, encoding="utf-8")
    print(f"wrote {len(joke)} chars to {OUT}")


if __name__ == "__main__":
    main()
