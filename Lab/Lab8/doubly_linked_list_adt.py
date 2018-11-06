# A Doubly Linked List abstract data type
#
# Written by Eric Martin and Ran Bai for COMP9021


from copy import deepcopy


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    # Creates a linked list possibly from a list of values.
    def __init__(self, L = None, key = lambda x: x):
        self.key = key
        if L is None:
            self.head = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node


    def print(self, separator = ', '):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.print(separator = ' : ')
        2 : 0 : 1 : 3 : 7
        >>> LL = DoublyLinkedList([1])
        >>> LL.print()
        1
        >>> LL = DoublyLinkedList([])
        >>> LL.print()
        '''
        list = []
        current = self.head
        while current:
            list.append(str(current.value))
            current = current.next_node
        if len(list) > 0:
            print(f"{separator.join(list)}")


    def duplicate(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL_copy = LL.duplicate()    
        >>> LL_copy.print()
        2, 0, 1, 3, 7
        '''
        list = []
        current = self.head
        while current:
            list.append(current.value)
            current = current.next_node
        LL_copy = DoublyLinkedList(L = list, key=self.key)
        return LL_copy


    def length(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.length())
        5
        '''
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next_node
        return length


    def apply_function(self, function):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.apply_function(lambda x: 2 * x)
        >>> LL.print()
        4, 0, 2, 6, 14
        '''
        current = self.head
        while current:
            current.value = function(current.value)
            current = current.next_node
        return


    def is_sorted(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.is_sorted())
        False
        '''
        current = self.head
        last_number = None
        while current:
            if last_number == None:
                last_number = current.value
            else:
                if last_number > current.value:
                    return False
                last_number = current.value
            current = current.next_node


    def extend(self, LL):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(LL.duplicate())
        >>> LL.print()
        2, 0, 1, 3, 7, 2, 0, 1, 3, 7
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(DoublyLinkedList([]))
        >>> LL.print()
        2, 0, 1, 3, 7
        '''
        current = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = LL.head


    def reverse(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7, 2, 0, 1, 3, 7])
        >>> LL.reverse()
        >>> LL.print()
        7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        current = self.head
        while current.next_node:
            current.next_node.previous_node = current
            current = current.next_node

        self.head = current
        while current:
            current.next_node = current.previous_node
            current.previous_node = None
            current = current.next_node


    def index_of_value(self, value):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.index_of_value(2))
        4
        >>> print(LL.index_of_value(5))
        -1
        '''
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next_node
            index += 1
        return -1


    def value_at(self, index):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.value_at(4))
        2
        >>> print(LL.value_at(10))
        None
        '''
        flag = 0
        current = self.head
        while current:
            if index == flag:
                return current.value
            current = current.next_node
            flag += 1
        return None


    def prepend(self, LL):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> LL.prepend(DoublyLinkedList([20, 21, 22]))
        >>> LL.print()
        20, 21, 22, 7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        current = LL.head
        while current.next_node:
            current = current.next_node

        current.next_node = self.head
        self.head = LL.head
        return


    def append(self, value):
        '''
        >>> LL = DoublyLinkedList()
        >>> LL.append(10)
        >>> LL.print()
        10
        >>> LL.append(15)
        >>> LL.print()
        10, 15
        >>> LL.append(18)
        >>> LL.print()
        10, 15, 18
        '''
        if self.head != None:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(value)
        else:
            self.head = Node(value)


    def insert_value_at(self, value, index):
        '''
        >>> LL = DoublyLinkedList([10, 15])
        >>> LL.insert_value_at(5, 0)
        >>> LL.insert_value_at(25, 3)
        >>> LL.insert_value_at(20, 3)
        >>> LL.print()
        5, 10, 15, 20, 25
        '''
        pos = 0
        current = self.head
        if index == 0:
            new = Node(value)
            new.next_node = current
            self.head = new
            return
        else:
            last = None
            while current:
                if pos == index - 1:
                   last = current
                if pos == index:
                    new = Node(value)
                    new.next_node = current
                    last.next_node = new
                    return
                current = current.next_node
                pos += 1

        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(value)


    def insert_value_before(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([5, 10, 15, 20, 25])
        >>> LL.insert_value_before(0, 5)
        True
        >>> LL.insert_value_before(30, 35)
        False
        >>> LL.insert_value_before(22, 25)
        True
        >>> LL.insert_value_before(7, 10)
        True
        >>> LL.print()
        0, 5, 7, 10, 15, 20, 22, 25
        '''
        current = self.head
        last = Node()
        last.next_node = self.head

        if self.head.value == value_2:
            new = Node(value_1)
            new.next_node = self.head
            self.head = new
            return True
        else:
            while current:
                if current.value == value_2:
                    new = Node(value_1)
                    last.next_node = new
                    new.next_node = current
                    return True
                current = current.next_node
                last = last.next_node
        return False


    def insert_value_after(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([0, 5, 7, 10, 15, 20, 22, 25])
        >>> LL.insert_value_after(3, 1)
        False
        >>> LL.insert_value_after(2, 0)
        True
        >>> LL.insert_value_after(12, 10)
        True
        >>> LL.insert_value_after(27, 25)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27
        
        '''
        current = self.head
        while current:
            if current.value == value_2:
                new = Node(value_1)
                new.next_node = current.next_node
                current.next_node = new
                return True
            current = current.next_node
        return False


    def insert_sorted_value(self, value):
        '''
        >>> LL = DoublyLinkedList([0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27])
        >>> LL.insert_sorted_value(-5)
        >>> LL.insert_sorted_value(17)
        >>> LL.insert_sorted_value(30)
        >>> LL.print()
        -5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30
        
        '''
        current = self.head
        last = Node()
        last.next_node = self.head

        if value < self.head.value:
            new = Node(value)
            new.next_node = current
            self.head = new
            return
        else:
            while current:
                if current.value > value:
                    new = Node(value)
                    last.next_node = new
                    new.next_node = current
                    return
                current = current.next_node
                last = last.next_node

        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(value)


    def delete_value(self, value):
        '''
        >>> LL = DoublyLinkedList([-5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30])
        >>> LL.delete_value(-5)
        True
        >>> LL.delete_value(30)
        True
        >>> LL.delete_value(15)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 17, 20, 22, 25, 27
        
        '''
        current = self.head
        last = Node()
        last.next_node = self.head

        if self.head.value == value:
            self.head = current.next_node
            return True
        else:
            while current:
                if current.value == value:
                    last.next_node = current.next_node
                    return True
                current = current.next_node
                last = last.next_node
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

