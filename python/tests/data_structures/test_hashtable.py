import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_dict(create_dict):
    hashtable = create_dict
    expected = "Used for apple sauce"
    assert expected == hashtable.get("apple")
    assert None == hashtable.get("pear")


# @pytest.mark.skip("TODO")
def test_set_dict(create_dict):
    hashtable = create_dict
    hashtable.set("pear", "Used for pear sauce")
    actual = hashtable.get("pear")
    expected = "Used for pear sauce"
    assert actual == expected


# @pytest.mark.skip('TODO')
def test_hash_dict(create_dict):
    expected = hash(100) % create_dict.size
    actual = create_dict.hash(100)
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_has_dict(create_dict):
    assert True == create_dict.has("apple")
    assert False == create_dict.has('pumpkin')


# @pytest.mark.skip("TODO")
def test_keys_dict(create_dict):
    actual = set(create_dict.keys())
    expected = set(['silent','ahmad','apple', 'listen'])
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals(create_dict):
    hashtable = create_dict
    actual_keys = set()
    actual_values = set()
    for items in hashtable.buckets:
        if len(items) > 0 and isinstance(items, list):
            for item in items:
                actual_keys.add(item[0])
                actual_values.add(item[1])
    expected_keys = set(['silent','ahmad','apple', 'listen'])
    expected_values = set([True,30,'Used for apple sauce','to me'])
    assert actual_keys == expected_keys
    assert actual_values == expected_values


@pytest.fixture
def create_dict():
    hashtable = Hashtable(1024)
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    return hashtable
