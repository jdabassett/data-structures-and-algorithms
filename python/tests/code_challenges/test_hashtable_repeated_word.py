import pytest
from collections import Counter
from data_structures.hashtable import Hashtable
from code_challenges.hashtable_repeated_word import first_repeated_word, word_count, word_sort, remove_punctuation_spaces_lower

# @pytest.mark.skip("TODO")
def test_remove_punctuation_space_convert():
    assert "" == remove_punctuation_spaces_lower()
    assert "apple" == remove_punctuation_spaces_lower("!@#$%&*^; apple :{]<>?/,.")
    with pytest.raises(TypeError):
        remove_punctuation_spaces_lower(1)

# @pytest.mark.skip("TODO")
def test_word_count():
    input_str = "a a b b c c c"
    expected = Counter(input_str.replace(" ",""))
    actual = word_count(input_str)
    for key,value in expected.items():
        if actual.get(key) != value:
            assert False
    assert "[]" == str(word_count(""))
    with pytest.raises(TypeError):
        word_count(1)


# @pytest.mark.skip("TODO")
def test_word_sort():
    input_str = "a b b c c c"
    expected = ["c","b","a"]
    actual = word_sort(input_str)
    assert actual == expected
    assert [] == word_sort("")
    with pytest.raises(TypeError):
        word_sort(1)


# @pytest.mark.skip("TODO")
def test_word_sort_blank():
    actual = word_sort("")
    expected = []
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected
