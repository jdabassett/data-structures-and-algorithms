from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    """"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    """"""
    def __init__(self, top: Node=None):
        self.top = top

    def push(self,value):
        """"""
        node_top = Node(value)
        node_top.next = self.top
        self.top = node_top

    def pop(self):
        """"""
        if isinstance(self.top,Node):
            node_top = self.top.next
            node_return = self.top
            self.top = node_top
            return node_return.value
        else:
            raise InvalidOperationError('Method not allowed on empty collection')

    def peek(self):
        """"""
        if isinstance(self.top,Node):
            return self.top.value
        else:
            raise InvalidOperationError('Method not allowed on empty collection')


    def is_empty(self):
        """"""
        if isinstance(self.top,Node):
            return False
        else:
            return True

