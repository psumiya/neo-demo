from neo_demo import slugify, word_count


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
