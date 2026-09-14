def is_palindrome(text):
    """Return True if text reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def reverse_words(text):
    """Return text with the order of its words reversed."""
    return " ".join(text.split()[::-1])
