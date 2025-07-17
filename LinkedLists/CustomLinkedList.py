'''
    Prepend O(1): Add at the beggining of the list
    Append O(1): Add at the end of the list
    Lookup O(n): Go through the list from the head till the tail (worst case)
    Insert O(n): One by one, find index and insert
    Delete O(n): Find the item
'''
'''
    LinkedList: 10-->5-->16
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    # O(1)
    def size(self):
        return f"{self.length}"

    # O(1)
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length = self.length + 1
        return self

    # O(1)
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length = self.length + 1

    # O(n)
    def print_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr

    # O(n)
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return self.print_list()

        if index >= self.length:
            self.append(value)
            return self.print_list()

        new_node = Node(value)
        current = self.head
        prev = None
        count = 0

        while current:
            if count == index:
                prev.next = new_node
                new_node.next = current
                return self.print_list()

            prev = current
            current = current.next
            count = count + 1

        print("Index out of bounds")
        return self.print_list()

    # O(n)
    def delete(self, index):
        # if index = 0, just remove the head
        if index == 0:
            self.head = self.head.next
            self.length = self.length - 1
            return print_list()
        
        # if index is more than a length, just print an error
        if index >= self.length:
            print("Index out of bounds")

        current = self.head
        prev = None
        count = 0
        while current:
            if index == count:
                prev.next = current.next
                self.length = self.length - 1
                return self.print_list()
            
            count = count + 1
            prev = current
            current = current.next

        print("Index out of bounds")
        return self.print_list()


def main():
    cll = LinkedList(10)
    cll.append(5)
    cll.append(16)
    cll.prepend(2)
    print(cll.print_list())
    print(cll.size())
    print(cll.insert(99, 13))
    print(cll.size())
    print(cll.delete(4))
    print(cll.size())


if __name__ == '__main__':
    main()
