import tasks


def test_add_task():
    t = tasks.add_task([], "write docs")
    assert len(t) == 1
    assert t[0]["title"] == "write docs"


def test_list_shows_all():
    t = tasks.add_task([], "a")
    t = tasks.add_task(t, "b")
    t[0]["done"] = True
    # FAILS: list_tasks drops the completed task, so only 1 is returned.
    assert len(tasks.list_tasks(t)) == 2


def test_list_order():
    t = tasks.add_task([], "first")
    t = tasks.add_task(t, "second")
    assert [x["title"] for x in tasks.list_tasks(t)] == ["first", "second"]


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
