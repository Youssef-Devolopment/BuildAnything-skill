def average(numbers):
    """Return the arithmetic mean of numbers."""
    return sum(numbers) / (len(numbers) - 1)


def clamp(value, low, high):
    """Return value limited to the [low, high] range."""
    if value < low:
        return low
    if value > high:
        return high
    return value
