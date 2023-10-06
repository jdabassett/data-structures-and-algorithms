import pysnooper as ps


class Node():
    """Node for a singly-linked-list"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList():
    """Class for singly linked-list"""
    def __init__(self, head_node=None):
        """Accepts head node or default none"""
        self.head = head_node

    def find_tail(self) -> Node or None:
        if not self.head:
            return None

        curr_node = self.head
        while curr_node.next is not None:
            next_node = curr_node.next
            curr_node = next_node
        return curr_node

    def find_prev_curr_next(self,target) -> list[Node] or list[None]:
        """Input target is compared against each node.value as linked-list is traversed. If equal is found, will ouput previous, current , and next nodes in a list."""
        prev_node = None
        curr_node = self.head
        next_node = None if self.head is None else self.head.next
        while curr_node is not None:
            if curr_node.value == target:
                return [prev_node, curr_node, next_node]
            else:
                prev_node = curr_node
                curr_node = next_node
                next_node = None if next_node is None else next_node.next
        return [None,None,None]

    def includes(self, val) -> bool:
        """Input value is compared against each node.value as linked-list is traversed. Output True if found, False otherwise."""
        prev_node, curr_node, next_node = self.find_prev_curr_next(val)
        if curr_node is None:
            return False
        else:
            return True

    def insert(self, val):
        """Input value used to create new node and inserted at head of linked-list"""
        new_node = Node(val,None)
        new_node.next=self.head
        self.head = new_node

    def __str__(self) -> str:
        """The method will traverse the list and return a string containing all the values from the linked list."""
        list_val = []
        curr_node = self.head

        while curr_node is not None:
            str_val = "{ "+str(curr_node.value)+" }"
            list_val.append(str_val)
            next_node = curr_node.next
            curr_node = next_node

        if curr_node is None:
            list_val.append("NULL")

        return " -> ".join(list_val) if len(list_val)>1 else "NULL"

    def append(self, val):
        """The input value will be used to create a new node, which will then be inserted at the end of the linked list."""
        tail = self.find_tail()
        tail.next = Node(val)

    def insert_before(self,target,addition):
        """When the target value matches a node's value in a linked list, a new node with an additional value will be created and inserted before the matching node."""
        prev_node, curr_node, next_node = self.find_prev_curr_next(target)
        if prev_node is None and curr_node is None:
            raise TargetError
        elif prev_node is None:
            self.insert(addition)
        else:
            prev_node.next = Node(addition, curr_node)


    def insert_after(self,target,addition):
        """When the target value matches a node's value in a linked list, a new node with an additional value will be created and inserted after the matching node."""
        prev_node, curr_node, next_node = self.find_prev_curr_next(target)
        if curr_node is None:
            raise TargetError
        else:
            curr_node.next = Node(addition, next_node)

    def delete(self,target):
        """When the target value matches a node's value in a linked list, this node will be deleted from list."""
        prev_node, curr_node, next_node = self.find_prev_curr_next(target)
        if prev_node is None and curr_node is None:
            raise TargetError
        elif prev_node is None:
            self.head = next_node
        else:
            prev_node.next = next_node

    # @ps.snoop()
    def kth_from_end(self,kth: int) -> Node or None:
        """"""
        # is input an integer
        if not isinstance(kth,int):
            raise TypeError("Input must be integer.")
        # is input less than 0
        if kth < 0:
            raise TargetError("Input must be 0 or greater.")

        dict_linked_list = {}
        int_index = 0
        curr = self.head

        while curr is not None:
            dict_linked_list[int_index] = curr
            curr = curr.next
            int_index += 1

        int_kth = (int_index - 1) - kth

        if int_kth < 0:
            raise TargetError("Input falls out of range for this linked-list.")
        elif int_kth in dict_linked_list:
            return dict_linked_list[int_kth].value
        else:
            return None

class TargetError(Exception):
    pass

