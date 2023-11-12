from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(obj_tree: KaryTree) -> KaryTree:
    """
    Function to accept Kary-Tree and return new modified Kary-Tree with node values replaced with 'FizzBuzz' if divisible by 15, 'Buzz' if divisible by 5, 'Fizz' if divisible by 3, and coverted to a string if anything else.
    """
    if not isinstance(obj_tree, KaryTree):
        raise ValueError('Must input Kary-Tree into "fizz_buzz_tree" function.')
    if hasattr(obj_tree, 'root') and obj_tree.root is None:
        return KaryTree(None)

    def helper(node_curr, node_new):
        if node_curr is None:
            return
        if node_curr.value % 15 == 0:
            node_new.value = 'FizzBuzz'
        elif node_curr.value % 5 == 0:
            node_new.value = "Buzz"
        elif node_curr.value % 3 == 0:
            node_new.value = "Fizz"
        else:
            node_new.value = str(node_curr.value)
        for child in node_curr.children:
            node_new.children.append(helper(child, Node()))
        return node_new

    node_return = helper(obj_tree.root, Node())
    return KaryTree(node_return)
