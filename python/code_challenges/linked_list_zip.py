from data_structures.linked_list import LinkedList, Node
import time

def zip_lists(a, b):
    node_curr_a = a.head
    node_curr_b = b.head

    if a.head is None and b.head is None:
        return LinkedList()

    node_dummy = Node()
    node_curr = node_dummy

    while node_curr_a is not None or node_curr_b is not None:
        if node_curr_a is not None:
            node_curr.next = node_curr_a
            node_curr = node_curr.next
            node_curr_a = node_curr_a.next
        if node_curr_b is not None:
            node_curr.next = node_curr_b
            node_curr = node_curr.next
            node_curr_b = node_curr_b.next

    return LinkedList(node_dummy.next)



# aa = LinkedList(Node(3))
# aa.insert(2)
# aa.insert(1)
# bb = LinkedList(Node('c'))
# bb.insert('b')
# bb.insert('a')
# # print(aa,bb)
# cc = zip_lists(aa,bb)
#
# print(cc)
