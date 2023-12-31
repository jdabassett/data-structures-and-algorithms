import pytest
from code_challenges.tree_intersection import tree_intersection, convert_tree_to_hashtable
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue
from data_structures.hashtable import Hashtable


# @pytest.mark.skip("TODO")
def test_tree_intersection(create_binary_trees, create_lists_values):
    tree_a, tree_b = create_binary_trees
    first, second, expected = create_lists_values
    actual = tree_intersection(tree_a, tree_b)
    assert len(actual) == len(expected)
    assert sorted(actual) == sorted(expected)
    assert isinstance(actual, list)

# @pytest.mark.skip("TODO")
def test_tree_intersection_empty():
    actual = tree_intersection(BinaryTree(),BinaryTree())
    assert actual == []


# @pytest.mark.skip("TODO")
def test_convert_tree_to_hashtable(create_lists_values):
    first, second, third = create_lists_values
    hashtable = convert_tree_to_hashtable(first)
    for value in first:
        assert hashtable.has(value)
    assert isinstance(hashtable, Hashtable)


# @pytest.mark.skip("TODO")
def test_convert_tree_to_hashtable_empty():
    hashtable = convert_tree_to_hashtable([])
    assert isinstance(hashtable, Hashtable)
    assert hashtable.convert_to_list() == []


@pytest.fixture()
def create_binary_trees():
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    return tree_a, tree_b


@pytest.fixture()
def create_lists_values():
    return [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500], [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500], [125, 175, 100, 160, 500, 200, 350]


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
