"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Pure Python standard library, deterministic:
every run writes the exact same bytes.

Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters,
not only whitespace.
"""

import os

RANT = (
    "I have clicked every traffic light, every crosswalk, every bicycle, "
    "and the website still does not believe I am human. "
    "I have spent longer proving I am a person than the actual task "
    "would have taken. "
    "A robot would have passed in four seconds. "
    "I am failing a test designed for robots at being a human, and "
    "honestly, the robot deserves the account."
)


def main() -> None:
    # Gate mirror: 1-400 characters and not only whitespace.
    if not 1 <= len(RANT) <= 400 or not RANT.strip():
        raise ValueError(f"rant is {len(RANT)} characters, must be 1-400")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(RANT)
    print(f"wrote /output/entry.txt ({len(RANT)} characters)")


if __name__ == "__main__":
    main()
