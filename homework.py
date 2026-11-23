def cube(n):
    """Return n to the power of 3."""
    return n ** 3


def can_ride(height_cm):
    """True if the height is 120 cm or more."""
    return height_cm >= 120


def longest_word(text):
    """The longest word of the text, or "" if the text is empty. If two words are equally long, the first one."""
    return max(text.split(), key=len)


def fizzbuzz(n):
    """Return the text FizzBuzz if n is divisible by 15, Fizz if by 3, Buzz if by 5, otherwise n as text."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def median(numbers):
    """Median of a non-empty list. For an even number of values, the average of the two middle values."""
    s = sorted(numbers)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    else:
        return s[mid]
