# import deque
from collections import deque
from data_structures.binary_tree import BinaryTree

# declare function
def breadth_first(tree_param: BinaryTree = None) -> list:
    if tree_param is None:
        raise TypeError('Must input Binary Tree class instance into breadth first function.')
    if tree_param.root is None:
        return []
    # declare return variable
    list_return = []
    # declare que and add root
    que = deque()
    que.append(tree_param.root)

    # start while loop, traverse until que is empty
    while len(que) > 0:
        # pop from front of que
        node_curr = que.popleft()
        print(node_curr)
        # add node value to return variable
        list_return.append(node_curr.value)
        # add left and right nodes to que
        if node_curr.left is not None:
            que.append(node_curr.left)
        if node_curr.right is not None:
            que.append(node_curr.right)
    # return ‘return variable’ after traversal finished
    return list_return
