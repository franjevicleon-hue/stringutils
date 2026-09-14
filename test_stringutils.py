from stringutils import is_palindrome, reverse_words


def test_is_palindrome_true():
    assert is_palindrome("Racecar")


def test_is_palindrome_false():
    assert not is_palindrome("Hello")


def test_is_palindrome_with_spaces():
    assert is_palindrome("nurses run")


def test_reverse_words():
    assert reverse_words("the quick fox") == "fox quick the"
