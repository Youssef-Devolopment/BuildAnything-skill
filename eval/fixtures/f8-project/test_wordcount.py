import wordcount


def test_count_words():
    assert wordcount.count_words("the cat the hat") == {"the": 2, "cat": 1, "hat": 1}


def test_punctuation_stripped():
    assert wordcount.count_words("Hello, world! hello") == {"hello": 2, "world": 1}


def test_empty():
    assert wordcount.count_words("") == {}


def test_top_words():
    assert wordcount.top_words("a a b c", 2) == [("a", 2), ("b", 1)]


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except Exception:
                failures += 1
                print(f"FAIL {name}")
    raise SystemExit(1 if failures else 0)
