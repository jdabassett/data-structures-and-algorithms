class BinaryTree:
    """
    Class to make binary trees.
    Attributes: root
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self)->list:
        """
        For the pre-order traversal of binary tree.
        """
        list_return = []

        def helper(curr_node):
            if curr_node is None:
                return
            list_return.append(curr_node.value)
            helper(curr_node.left)
            helper(curr_node.right)

        helper(self.root)
        return list_return

    def in_order(self)->list:
        """
        For the in-order traversal of binary tree.
        """
        list_return = []

        def helper(curr_node):
            if curr_node is None:
                return
            helper(curr_node.left)
            list_return.append(curr_node.value)
            helper(curr_node.right)

        helper(self.root)
        return list_return

    def post_order(self)->list:
        """
        For the post-order traversal of binary tree.
        """
        list_return = []

        def helper(curr_node):
            if curr_node is None:
                return
            helper(curr_node.left)
            helper(curr_node.right)
            list_return.append(curr_node.value)

        helper(self.root)
        return list_return

    def find_maximum_value(self)->int or float:
        if self.root is None:
            raise TreeEmptyError()
        num_max = -float('inf')
        def helper(node_curr, par_max):
            if node_curr is None:
                return par_max
            if node_curr.value > par_max:
                par_max = node_curr.value
            return max(helper(node_curr.left,par_max), helper(node_curr.right,par_max))
        return helper(self.root, num_max)




class Node:
    """
    Class to make nodes for a binary tree.
    Attributes: Value, Left(left node), Right(right node)
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1
        self.count = 1

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

    def __lt__(self,other):
        if isinstance(other,Node):
            if self.value <= other.value:
                return True
            else:
                return False
        else:
            raise TypeError('Objects of different classes cannot be compared.')

    def __gt__(self, other):
        if isinstance(other, Node):
            if self.value >= other.value:
                return True
            else:
                return False
        else:
            raise TypeError('Objects of different classes cannot be compared.')


    def __eq__(self, other):
        if isinstance(other, Node):
            if self.value == other.value:
                return True
            else:
                return False
        else:
            raise TypeError('Objects of different classes cannot be compared.')


class TreeEmptyError(Exception):
    def __init__(self,message="Tree is empty"):
        super().__init__(message)
