from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree0: BinaryTree, tree1: BinaryTree) -> list[int]:
    """
    Input two binary trees.
    Output is a list of values shared by both trees.
    """
    values0 = tree0.in_order()
    values1 = tree1.in_order()
    hashtable0 = convert_tree_to_hashtable(values0)
    hashtable1 = convert_tree_to_hashtable(values1)

    return_values = []
    for value in values0:
        if hashtable1.has(value) and hashtable0.get(value) == 1:
            return_values.append(value)
    return return_values


def convert_tree_to_hashtable(values: list[int]) -> Hashtable:
    """
    Input list of values.
    Output Hashtable with count of each value in list.
    """
    hashtable = Hashtable()
    for value in values:
        if hashtable.has(value):
            hashtable.update(value, 1)
        else:
            hashtable.set(value,1)
    return hashtable
