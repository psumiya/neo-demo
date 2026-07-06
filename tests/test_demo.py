import pytest

from neo_demo import slugify, truncate, word_count


def test_slugify_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_symbols():
    assert slugify("a  --  b__c") == "a-b-c"


def test_slugify_empty():
    assert slugify("") == ""


def test_word_count():
    assert word_count("one two  three") == 3


def test_word_count_empty():
    assert word_count("") == 0


def test_truncate_unchanged():
    assert truncate("hi", 10) == "hi"


def test_truncate_exact_length():
    assert truncate("hello", 5) == "hello"


def test_truncate_cuts_with_ellipsis():
    assert truncate("Hello, World!", 7) == "Hello,…"


def test_truncate_max_len_one():
    assert truncate("abc", 1) == "…"


def test_truncate_invalid_max_len():
    with pytest.raises(ValueError):
        truncate("text", 0)
