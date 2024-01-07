import pytest
from code_challenges.hashtable_left_join import left_join


# @pytest.mark.skip("TODO")
def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_left_join_fail():
    with pytest.raises(TypeError):
        left_join("", {})
        left_join("", "")


# @pytest.mark.skip("TODO")
def test_left_join_success(create_dictionaries):
    synonyms, antonyms, expected = create_dictionaries
    actual = left_join(synonyms, antonyms)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_left_join_all_keys_remain(create_dictionaries):
    synonyms, antonyms, expected = create_dictionaries
    actual = left_join(synonyms, antonyms)
    list_bool = [True if key in actual else False for key in synonyms.keys()]
    assert all(list_bool), "Some keys from first input dictionary not found in output dictionary."


@pytest.fixture()
def create_dictionaries():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = {'diligent': {'synonym': 'employed', 'antonym': 'idle'}, 'fond': {'synonym': 'enamored', 'antonym': 'averse'}, 'guide': {'synonym': 'usher', 'antonym': 'follow'}, 'outfit': {'synonym': 'garb', 'antonym': None}, 'wrath': {'synonym': 'anger', 'antonym': 'delight'}}

    return synonyms, antonyms, expected
