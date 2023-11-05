import pytest
from data_structures.binary_tree import BinaryTree, Node, TreeEmptyError


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

# @pytest.mark.skip('TODO')
def test_empty_binary_tree():
    tree = BinaryTree()

    with pytest.raises(TreeEmptyError):
        actual = tree.find_maximum_value()
