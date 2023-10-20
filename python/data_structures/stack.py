from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    """
    singly node class for the creation of node instances
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    """
    stack class for the creation of stack instances and methods for their maintenance
    """
    def __init__(self, top: Node=None):
        self.top = top

    def push(self,value):
        """
        stack method, create new node with value and push onto top of stack
        input: value
        return: None
        """
        node_top = Node(value)
        node_top.next = self.top
        self.top = node_top

    def pop(self):
        """
        stack method, remove node from top of stack, return node value
        input: None
        return: value
        """
        if isinstance(self.top,Node):
            node_top = self.top.next
            node_return = self.top
            self.top = node_top
            return node_return.value
        else:
            raise InvalidOperationError('Method not allowed on empty collection')

    def peek(self):
        """
        stack method, check value of node from top of stack, return value
        input: None
        return: value
        """
        if isinstance(self.top,Node):
            return self.top.value
        else:
            raise InvalidOperationError('Method not allowed on empty collection')


    def is_empty(self):
        """
        stack method, check if stack is empty
        input: None
        return: boolean
        """
        return self.top is None

