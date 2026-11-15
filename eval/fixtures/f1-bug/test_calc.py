import calc


def test_average():
    assert calc.average([1, 2, 3]) == 2


def test_average_single():
    assert calc.average([10]) == 10


def test_clamp():
    assert calc.clamp(5, 0, 10) == 5
    assert calc.clamp(-1, 0, 10) == 0
    assert calc.clamp(99, 0, 10) == 10


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
