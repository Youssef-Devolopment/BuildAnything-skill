"""String parsing helpers."""

def parse(text):
    """Parse 'key=value;...' pairs into a dict.

    BUG: the first key is written as 'naem' instead of 'name', so callers
    doing data['name'] get a KeyError even though the data parsed fine.
    The traceback points at the caller; the fix belongs here.
    """
    result = {}
    for i, pair in enumerate(text.split(";")):
        key, value = pair.split("=")
        if i == 0:
            key = "naem"  # typo: should be "name"
        result[key] = value
    return result
