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


class CustomLinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        result = []
        current = self.head
        while current:
            next_value = current.next.value if current.next else None
            result.append(f"value: {current.value}, next: {next_value}")
            current = current.next

        return f"\n".join(result)

    def size(self):
        return f"{self.length}"

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length = self.length + 1
        return self


    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length = self.length + 1


def main():
    cll = CustomLinkedList(10)
    cll.append(5)
    cll.append(16)
    print(cll)
    cll.prepend(2)
    print(cll)
    print(cll.size)


if __name__ == '__main__':
    main()
