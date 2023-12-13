from collections import deque


def merge_sort(unsorted: list[int]) -> list[int]:
    int_len = len(unsorted)
    list_input = unsorted
    list_sorted = []
    if int_len > 1:
        int_mid = int_len // 2
        list_left = list_input[0:int_mid]
        list_right = list_input[int_mid:]
        list_left = merge_sort(list_left)
        list_right = merge_sort(list_right)
        list_sorted = merge(list_left, list_right)
    return list_sorted or list_input


def merge(left: list[int], right: list[int]) -> list[int]:
    que_left = deque(left or [])
    que_right = deque(right or [])
    que_return = deque()
    while len(que_left) > 0 and len(que_right) > 0:
        if que_left[0] < que_right[0]:
            que_return.append(que_left.popleft())
        else:
            que_return.append(que_right.popleft())

    if len(que_left) == 0:
        return [*que_return, *que_right]
    else:
        return [*que_return, *que_left]


# if __name__=="__main__":
#     list0 = [8, 4, 23, 42, 16, 15]
#     list1 = [20, 18, 12, 8, 5, -2]
#     list2 = [5, 12, 7, 5, 5, 7]
#     list3 = [2, 3, 5, 7, 13, 11]
#     lists = [list0, list1, list2, list3]
#     for each in lists:
#         print(merge_sort(each))
