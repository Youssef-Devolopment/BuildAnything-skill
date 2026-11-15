"""Word counting library with a CLI."""

import sys
from collections import Counter


def count_words(text):
    """Return a Counter of lowercased words in text."""
    words = [w.strip(".,!?;:\"'()").lower() for w in text.split()]
    return Counter(w for w in words if w)


def top_words(text, n=3):
    """Return the n most common (word, count) pairs."""
    return count_words(text).most_common(n)


def main(argv):
    if len(argv) != 1:
        print("usage: python wordcount.py <file>", file=sys.stderr)
        return 2
    try:
        with open(argv[0], encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    for word, count in top_words(text):
        print(f"{word}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
