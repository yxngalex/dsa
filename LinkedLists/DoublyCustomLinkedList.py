'''
    Prepend O(1): Add at the beggining of the list
    Append O(1): Add at the end of the list
    Lookup O(n): Go through the list from the head till the tail (worst case)
    Insert O(n): One by one, find index and insert
    Delete O(n): Find the item
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        prev = self.previous.value if self.previous else None
        next = self.next.value if self.next else None
        return f"(Prev: {prev} <- {self.value} -> Next: {next}"


class DoublyLinkedList():
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
        new_node.previous = self.tail # Set new nodes previous to be the current tail, before we add a new node
        self.tail.next = new_node # Set the current tails next pointer to points to new node
        self.tail = new_node # Set the new tail to new node
        self.length = self.length + 1 # Increase len
        return self

    # O(1)
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head # Set new nodes pointer to the current head node
        self.head.previous = new_node # Set previous pointer to the new node
        self.head = new_node # Set head as a new node
        self.length = self.length + 1 # Increase len

    # O(n)
    def print_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(repr(current))
            current = current.next
        return arr

    # O(n)
    def insert(self, index, value):
        # if index is 0 add at the start of the list
        if index == 0:
            self.prepend(value)
            return self.print_list()

        # if index > len add at the end of the list
        if index >= self.length: 
            self.append(value)
            return self.print_list()

        new_node = Node(value)
        current = self.head
        count = 0

        while current:
            if count == index:
                previous_node = current.previous

                previous_node.next = new_node
                new_node.previous = previous_node

                new_node.next = current
                current.previous = new_node

                self.length += 1
                return self.print_list()

            current = current.next
            count += 1

        print("Index out of bounds")
        return self.print_list()

    # O(n)
    def delete(self, index):
        # if index is more than a length, just print an error
        if index < 0 or index >= self.length:
            print("Index out of bounds")
            return self.print_list()

        # if index = 0, just remove the head
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None # List is empty
            self.length -= 1
            return self.print_list()
        

        current = self.head
        count = 0
        while current:
            if index == count:
                previous_node = current.previous
                next_node = current.next

                previous_node.next = next_node

                # If next_node exists, set his previous as previous_node
                if next_node:
                    next_node.previous = previous_node
                else: # If not, set previous_node as tail
                    self.tail = previous_node


                self.length -= 1
                return self.print_list()
            
            count += 1
            current = current.next

        print("Index out of bounds")
        return self.print_list()

    # Reverse tail and head using previous
    # O(N)
    def reverse(self):
        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = self.head.next

        while second:
            tmp = second.next
            second.next = first
            first = second
            second = tmp

        self.head.next = None
        self.head = first
        return self.print_list()

def main():
    cll = DoublyLinkedList(10)
    cll.append(5)
    cll.append(16)
    print(cll.print_list())
    cll.prepend(2)
    print(cll.print_list())
    print(cll.size())
    print(cll.insert(99, 88))
    # print(cll.print_list())
    # print(cll.delete(4))
    # print(cll.size())
    print(cll.reverse())


if __name__ == '__main__':
    main()
