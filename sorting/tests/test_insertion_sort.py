import pytest
from insertion.insertion_sort import insertion_sort
import random


# @pytest.mark.skip('TODO')
def test_insertion_sort(create_unsorted_lists):
    for unsorted in create_unsorted_lists:
        expected = sorted(unsorted)
        actual = insertion_sort(unsorted)
        assert expected == actual


@pytest.fixture()
def create_unsorted_lists():
    list_lists = list()
    for _ in range(0, 10):
        int_min = random.randint(-100,0)
        int_max = random.randint(1,10)
        int_inc = random.randint(1, 100)
        list_new = list(range(int_min, int_max, int_inc))
        random.shuffle(list_new)
        list_lists.append(list_new)
    list_lists.append([20, 18, 12, 8, 5, -2])
    list_lists.append([5, 12, 7, 5, 5, 7])
    list_lists.append([2, 3, 5, 7, 13, 11])
    return list_lists


