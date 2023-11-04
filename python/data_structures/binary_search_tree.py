from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    """

    def __init__(self,root):
        super().__init__(root)

    def add(self,value=None):
        # if no value is supplied
        if value:
            Node(value)
        else:
            # TODO: handler exception

        # if attempting to add to an empty tree
        if self.root is None:
            return BinarySearchTree(Node(value))




    def contains(self,value)->bool:
        pass
