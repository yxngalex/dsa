class StackQueue():
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self, value):
        self.last.append(value)

    def dequeue(self):
        if not self.first:
            while self.last:
                self.first.append(self.last.pop())

        if not self.first:
            raise IndexError('Queue is empty')

        return self.first.pop()

    def peek(self):
        if not self.first:
            while self.last:
                self.first.append(self.last.pop())

        if not self.first:
            return None

        return self.first[-1]


if __name__ == '__main__':
    q = Queue()
    print("peek 1, ", q.peek())
    q.enqueue("Joy")
    q.enqueue("Matt")
    q.enqueue("Pavel")
    print("peek 2, ", q.peek())
    print("==========")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("==========")
    print("peek 3, ", q.peek())
