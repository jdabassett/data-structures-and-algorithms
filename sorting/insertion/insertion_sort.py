def insertion(list_sorted: list[int], insertion_value: int) -> list[int]:
    for index, temporary_value in enumerate(list_sorted):
        if insertion_value < temporary_value:
            list_sorted[index] = insertion_value
            insertion_value = temporary_value
    list_sorted.append(insertion_value)
    return list_sorted


def insertion_sort(list_unsorted: list[int]) -> list[int]:
    list_sorted = [list_unsorted[0]]
    for i in range(1, len(list_unsorted)):
        insertion_value = list_unsorted[i]
        list_sorted = insertion(list_sorted, insertion_value)
    return list_sorted


if __name__ == "__main__":
    list_lists = list()
    list_lists.append([20, 18, 12, 8, 5, -2])
    list_lists.append([5, 12, 7, 5, 5, 7])
    list_lists.append([2, 3, 5, 7, 13, 11])

    for unsorted in list_lists:
        expected = sorted(unsorted)
        actual = insertion_sort(unsorted)
        assert expected == actual
