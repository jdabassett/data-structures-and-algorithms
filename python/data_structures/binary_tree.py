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
            list_return.append(curr_node.val)
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
            list_return.append(curr_node.val)
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
            list_return.append(curr_node.val)

        helper(self.root)
        return list_return


class Node:
    """
    Class to make nodes for a binary tree.
    Attributes: Value, Left(left node), Right(right node)
    """
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

    def __str__(self):
        return f"{self.val}"

    def __lt__(self,other):
        if isinstance(other,Node):
            if self.val <= other.val:
                return True
            else:
                return False
        else:
            # TODO: handler exception

    def __gt__(self, other):
        if isinstance(other, Node):
            if self.val >= other.val:
                return True
            else:
                return False
        else:
            # TODO: handler exception

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.val == other.val:
                return True
            else:
                return False
        else:
            # TODO: handler exception


