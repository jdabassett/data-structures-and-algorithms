import pytest
from merge.merge_sort import merge_sort
import random


# @pytest.skip.mark("TODO")
def test_merge_sort(create_unsorted_lists):
    for unsorted in create_unsorted_lists:
        expected = sorted(unsorted)
        actual = merge_sort(unsorted)
        assert expected == actual


@pytest.fixture()
def create_unsorted_lists():
    list_lists = []
    for _ in range(0, 10):
        int_min = random.randint(-100, 0)
        int_max = random.randint(1, 10)
        int_inc = random.randint(1, 100)
        list_new = list(range(int_min, int_max, int_inc))
        random.shuffle(list_new)
        list_lists.append(list_new)
    list_lists.append([8, 4, 23, 42, 16, 15])
    list_lists.append([20, 18, 12, 8, 5, -2])
    list_lists.append([5, 12, 7, 5, 5, 7])
    list_lists.append([2, 3, 5, 7, 13, 11])
    return list_lists
