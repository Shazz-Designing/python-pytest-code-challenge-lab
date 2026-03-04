from palindrome import longest_palindromic_substring


def test_simple_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_even_palindrome():
    assert longest_palindromic_substring("abba") == "abba"


def test_palindrome_in_middle():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_single_character():
    assert longest_palindromic_substring("a") == "a"