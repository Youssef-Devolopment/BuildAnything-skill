"""App configuration. The bug lives here: greeting() indexes wrong."""

def greeting(name):
    # BUG: dict lookup uses a key that does not exist; "name" is the real key.
    # Running app.py raises KeyError here (well, actually let's make the
    # failure happen at call time so the traceback ends in app.py).
    return "Hello, " + name.upper()
