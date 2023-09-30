
class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, head_node=None):
        self.head = head_node

    def insert(self, val):
        # try:
            new_node = Node(val,None)
            new_node.next=self.head
            self.head = new_node
        # except Exception:
        #     raise Exception(f"Exception: LinkedList.insert() unable to insert {val} into linked list instance.")

    def includes(self, val) -> bool:
        # try:
            curr_node = self.head
            while curr_node is not None:
                if curr_node.value == val:
                    return True
                next_node = curr_node.next
                curr_node = next_node
            return False
        # except Exception:
        #     raise Exception(f"Exception: LinkedList.includes() unable to verify that linked list instance includes {val}")

    def __str__(self) -> str:
        # try:
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
        # except Exception:
        #     raise Exception(f"Exception: LinkedList._str__() unable to generate string representation of link list.")
        #




class TargetError(Exception):
    pass

