"""Office Joke Open entry: writes one office joke to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

JOKE = (
    "I scheduled a meeting about having too many meetings. "
    "It got rescheduled \u2014 everyone was stuck in another meeting."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")
    print(f"Wrote joke ({len(JOKE)} chars) to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
