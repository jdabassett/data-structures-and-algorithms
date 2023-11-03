class BinaryTree:
    """
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        list_return = []

        def helper(curr_node):
            if curr_node is None:
                return
            list_return.append(curr_node.val)
            helper(curr_node.left)
            helper(curr_node.right)

        helper(self.root)
        return list_return

    def in_order(self):
        list_return = []

        def helper(curr_node):
            if curr_node is None:
                return
            helper(curr_node.left)
            list_return.append(curr_node.val)
            helper(curr_node.right)

        helper(self.root)
        return list_return

    def post_order(self):
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
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

    def __str__(self):
        return f"{self.val}"

