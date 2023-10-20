from data_structures.stack import Stack,Node
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.stack_enqueue = Stack(None)
        self.stack_dequeue = Stack(None)

    def enqueue(self,value):
        if not self.stack_dequeue.is_empty():
            while not self.stack_dequeue.is_empty():
                transfer_value = self.stack_dequeue.pop()
                self.stack_enqueue.push(transfer_value)
        self.stack_enqueue.push(value)


    def dequeue(self):
        if not self.stack_enqueue.is_empty():
            while not self.stack_enqueue.is_empty():
                transfer_value = self.stack_enqueue.pop()
                self.stack_dequeue.push(transfer_value)
        if self.stack_dequeue.is_empty():
            raise InvalidOperationError("Cannot dequeue from an empty queue.")
        else:
            return self.stack_dequeue.pop()

