
from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        # Replace pass above with your code
        temp = set()
        current = self.head
        while current:
            temp.add(current.value)
            current = current.next_node

        if len(temp) > 0:
            self.head.value = temp.pop()
            current = self.head
            while len(temp) != 0:
                current = current.next_node
                current.value = temp.pop()
            current.next_node = None
            
