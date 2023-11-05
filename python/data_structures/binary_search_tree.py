from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Create and manage binary search tree.
    Inherits from binary tree class.
    """

    def __init__(self,root=None):
        super().__init__(root)

    def add(self, value):
        """
        Method to add new value to binary search tree.
        Citation: ChatGPT inspired
        """
        self.root = self._insert(self.root, Node(value))

    def _insert(self, node_curr, node_insert):
        """
        Private method to insert new node into binary search tree and re-balance.
        Citation: ChatGPT inspired
        """
        if node_curr is None:
            return node_insert

        if node_insert == node_curr:
            node_curr.count += 1
        elif node_insert < node_curr:
            node_curr.left = self._insert(node_curr.left, node_insert)
        else:
            node_curr.right = self._insert(node_curr.right, node_insert)

        node_curr.height = 1 + max(self._get_height(node_curr.left), self._get_height(node_curr.right))

        return self._balance(node_curr)

    def _balance(self, node):
        """
        Checks and re-balances tree based on need.
        Can only handle re-balancing after singular addition.
        Citation: ChatGPT inspired
        """
        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z1):
        """
        Re-balance binary search tree.
        Moves current node down to left node of 'current node's right node'.
        Citation: ChatGPT inspired
        """
        y1 = z1.right
        x1 = y1.left

        y1.left = z1
        z1.right = x1

        z1.height = 1 + max(self._get_height(z1.left), self._get_height(z1.right))
        y1.height = 1 + max(self._get_height(y1.left), self._get_height(y1.right))

        return y1

    def _right_rotate(self, z1):
        """
        Re-balance binary search tree.
        Moves current node down to right node of 'current node's right node'.
        Citation: ChatGPT inspired
        """
        y1 = z1.left
        x1 = y1.right

        y1.right = z1
        z1.left = x1

        z1.height = 1 + max(self._get_height(z1.left), self._get_height(z1.right))
        y1.height = 1 + max(self._get_height(y1.left), self._get_height(y1.right))

        return y1

    def _get_height(self, node):
        """
        Private method to return height of node.
        Citation: ChatGPT inspired
        """
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        """
        Private method to return difference in heights between adjacent nodes
        Citation: ChatGPT inspired
        """
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def contains(self,value=None)->bool:
        """
        Checks binary search tree for input 'value'.
        If found, returns True. Returns False otherwise.
        """
        if value is None:
            raise ValueError('Must supply value to check if Binary Search Tree contains it.')

        def helper(node_curr, val):
            if node_curr is None:
                return False
            if node_curr.value == val:
                return True
            bool_left = helper(node_curr.left, val)
            bool_right = helper(node_curr.right, val)
            return bool_left or bool_right
        return helper(self.root, value)

    def print_tree(self,str_type='in'):
        """
        Prints to console representation of binary search tree based on type specified in input.
        Input: 'in' for 'in order' (default)
        Input: 'pre' for 'pre-order'
        Input: 'post' for 'post-order'
        """
        list_return = []
        if str_type == 'pre':
            list_return = self.pre_order()
        elif str_type == 'post':
            list_return = self.post_order()
        else:
            list_return = self.in_order()
        print(list_return)

if __name__=="__main__":
    bs3 = Node(3)
    bst = BinarySearchTree(bs3)
    bst.add(1)
    bst.add(5)
    bst.add(7)
    bst.print_tree('in')






##################################################################################3
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.height = 1
#         self.count = 1  # Number of nodes with the same value
#
#
# class BalancedBST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#
#     def _insert(self, node, key):
#         if node is None:
#             return Node(key)
#
#         if key == node.key:
#             node.count += 1
#         elif key < node.key:
#             node.left = self._insert(node.left, key)
#         else:
#             node.right = self._insert(node.right, key)
#
#         node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
#
#         return self._balance(node)
#
#     def _balance(self, node):
#         balance = self._get_balance(node)
#
#         if balance > 1:
#             if self._get_balance(node.left) < 0:
#                 node.left = self._left_rotate(node.left)
#             return self._right_rotate(node)
#
#         if balance < -1:
#             if self._get_balance(node.right) > 0:
#                 node.right = self._right_rotate(node.right)
#             return self._left_rotate(node)
#
#         return node
#
#     def _left_rotate(self, z):
#         y = z.right
#         T2 = y.left
#
#         y.left = z
#         z.right = T2
#
#         z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
#         y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
#
#         return y
#
#     def _right_rotate(self, y):
#         x = y.left
#         T2 = x.right
#
#         x.right = y
#         y.left = T2
#
#         y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
#         x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
#
#         return x
#
#     def _get_height(self, node):
#         if node is None:
#             return 0
#         return node.height
#
#     def _get_balance(self, node):
#         if node is None:
#             return 0
#         return self._get_height(node.left) - self._get_height(node.right)
#
#     def _inorder_traversal(self, node):
#         if node is not None:
#             self._inorder_traversal(node.left)
#             for _ in range(node.count):
#                 print(node.key, end=" ")
#             self._inorder_traversal(node.right)
#
#     def print_tree(self):
#         self._inorder_traversal(self.root)
#
#
# # Example usage:
# bst = BalancedBST()
# values = [10, 20, 30, 10, 50, 20]
# for value in values:
#     bst.insert(value)
#
# bst.print_tree()  # Output: 10 10 20 20 30 50
