class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        arr = []
        current = self.first
        while current:
            arr.append(str(current.value))
            current = current.next
        return ', '.join(arr)

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():  # if it's empty, first and last have the same node
            self.first = new_node
            self.last = self.first
        else:  # if it's not, set the pointer of last node to the new node, and then set the new node to be the last one
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        if self.first.value == self.last.value:
            self.last = None

        first = self.first
        self.first = self.first.next
        self.size -= 1
        return first.value


if __name__ == '__main__':
    q = Queue()
    print("peek, ", q.peek())
    q.enqueue("Joy")
    q.enqueue("Matt")
    q.enqueue("Pavel")
    q.enqueue("Samir")
    print("queue", q)
    print("peek, ", q.peek())
    print("dequeue: ", q.dequeue())
    print("queue", q)
    print("dequeue: ", q.dequeue())
    print("queue", q)
    print("dequeue: ", q.dequeue())
    print("queue", q)
    print("dequeue: ", q.dequeue())
    print("queue", q)
