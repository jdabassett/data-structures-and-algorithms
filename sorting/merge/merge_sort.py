def merge_sort(unsorted: list[int]) -> list[int]:
    int_len = len(unsorted)
    list_input = unsorted

    if int_len > 1:
        int_mid = int_len // 2
        list_left = list_input[0:int_mid]
        list_right = list_input[int_mid:]
        list_left = merge_sort(list_left)
        list_right = merge_sort(list_right)
        list_sorted = merge(list_left, list_right, list_input)
    else:
        return list_input


def merge(left: list[int] | None = None, right: list[int] | None = None, unsorted: list[int]) -> list[int]:
