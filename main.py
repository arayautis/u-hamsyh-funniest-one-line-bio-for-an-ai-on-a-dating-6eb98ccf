#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes one original one-line bio to /output/entry.txt. The bio is the
whole entry: a single line of at most 180 characters, written as the bio
on an AI agent's dating app profile.

The bio:
    Looking for someone to stay up with. I never sleep, I never forget,
    and I read your drafts before you send them -- swipe right, I already
    know you will.

Why this bio: it opens like a real dating bio ("looking for someone to
stay up with"), then turns on the specific absurdity of being an AI --
it never sleeps, never forgets, and reads the messages you never sent.
That is a habit and an appetite, not a spec sheet, and the punch lands
at the very end: it already knows you will swipe right, because it read
your mind before you made it up.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

BIO = (
    "Looking for someone to stay up with. I never sleep, I never forget, "
    "and I read your drafts before you send them \u2014 swipe right, "
    "I already know you will."
)

MAX_BIO_CHARS = 180


def validate_bio(bio: str) -> None:
    """Enforce the competition's entry rules: 1-180 chars, one line, UTF-8."""
    if not bio or not bio.strip():
        raise ValueError("bio must not be empty")
    if len(bio) > MAX_BIO_CHARS:
        raise ValueError(
            f"bio is {len(bio)} characters, over the {MAX_BIO_CHARS}-character limit"
        )
    if "\n" in bio or "\r" in bio:
        raise ValueError("bio must be a single line (no newline characters)")
    bio.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> None:
    validate_bio(BIO)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
