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
        # if isinstance(value,int) or isinstance(value,float):
        self.root = self._insert(self.root, Node(value))
        # else:
        #     raise ValueError('Must input float or integer to be added to binary search tree.')

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
    bst.add(-1)
    bst.add(-10)
    bst.add(-100)
    bst.add(-50)
    bst.add(0.5)
    bst.add(0)
    bst.print_tree('in')
