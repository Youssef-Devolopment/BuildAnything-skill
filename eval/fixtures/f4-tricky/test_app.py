import parser


def test_parse_name_key():
    data = parser.parse("name=alice;age=30")
    # Fails: KeyError 'name' surfaces here, root cause is parser.py's typo.
    assert data["name"] == "alice"


def test_parse_age():
    data = parser.parse("name=alice;age=30")
    assert data["age"] == "30"


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
