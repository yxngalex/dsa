class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def __str__(self):
        arr = []
        current = self.top
        while current:
            arr.append(current.value)
            current = current.next
        return str(arr)

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.value

    def push(self, value):
        node = Node(value)
        if self.isEmpty():
            self.top = node
            self.bottom = node
        else:
            currentTopPointer = self.top
            self.top = node
            self.top.next = currentTopPointer
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None

        if self.top == self.bottom:
            self.bottom = None

        currentTopPointer = self.top
        self.top = self.top.next
        self.size -= 1

        return currentTopPointer.value


def main():
    myStack = Stack()
    myStack.push('matthew')
    myStack.push('marko')
    myStack.push('alex')
    print("myStack after push:", myStack)
    print("Peek: ", myStack.peek())
    print("Popped: ", myStack.pop())
    print("myStack after pop:", myStack)
    print("Popped: ", myStack.pop())
    print("myStack after pop:", myStack)


if __name__ == '__main__':
    main()
