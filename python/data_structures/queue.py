
from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    """
    singly node class for creation of their instances
    """
    def __init__(self,value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    queue class for the creation of their instances and methods for their maintenance
    """

    def __init__(self, node = None):
        self.front = node
        self.back = self.front

    def enqueue(self,value):
        """
        queue method, create new nodes with value argument and add to back of queue
        input: value
        return: None
        """
        if self.front is None:
            node_back = Node(value,None)
            self.front = node_back
            self.back = node_back
        else:
            node_back = Node(value, self.back)
            self.back = node_back

    def dequeue(self):
        """
        queue method, remove nodes from front of queue, return node value
        input: None
        return: value
        """
        if self.front is None:
            raise InvalidOperationError("Cannot remove from an empty queue.")
        elif self.front == self.back:
            node_return = self.front
            self.front = None
            self.back = None
            return node_return.value
        else:
            node_curr = self.back
            node_prev = None
            while node_curr.next:
                node_prev = node_curr
                node_curr = node_curr.next

            self.front = node_prev
            self.front.next = None

            return node_curr.value


    def peek(self):
        """
        queue method, checks value of node at front of queue, returns value
        input: None
        return: value
        """
        if self.front is None:
            raise InvalidOperationError("Cannot peek from an empty queue.")
        else:
            node_return = self.front
            return node_return.value


    def is_empty(self):
        """
        queue method, checks if queue is empty
        input: None
        return: boolean
        """
        return self.front is None


