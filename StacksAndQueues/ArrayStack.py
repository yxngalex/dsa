class Stack:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def isEmpty(self):
        return len(self.array) == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.array.pop()


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
