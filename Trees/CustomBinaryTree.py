from Trees.bst_display import display


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value) if value is not None else None
        else:
            self.root = None

    # This is one way of doing it, introducing the parent node, which after iterating the whole tree,
    # we get the parent and then we add it to the left or to the right
    #
    # def insert(self, value):
    #     if not self.root:
    #         self.root = Node(value)
    #         return
    #
    #     current = self.root
    #     parent = None
    #
    #     while current:
    #         parent = current
    #         # Left
    #         if current.value > value:
    #             current = current.left
    #         # Right
    #         elif current.value < value:
    #             current = current.right
    #         else:
    #             return
    #
    #     if value < parent.value:
    #         parent.left = Node(value)
    #     if value > parent.value:
    #         parent.right = Node(value)

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if value < current.value:
                    # Left
                    if not current.left:
                        current.left = newNode
                        return self
                    current = current.left  # current becomes the left node
                elif value > current.value:
                    # Right
                    if not current.right:
                        current.right = newNode
                        return self
                    current = current.right  # current becomes the left node
                else:
                    return self

    def lookup(self, value):
        if not self.root:
            return False
        else:
            current = self.root
            while current:
                if value < current.value:
                    current = current.left
                elif value > current.value:
                    current = current.right
                elif value == current.value:
                    return current.value  # Or can return just current
            return False

    def remove(self, value):
        if not self.root:
            return None

        current = self.root
        parent = None
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            elif value == current.value:
                # We have 3 cases here:
                # 1. No right child
                # 2. Right child without a left child
                # 3. Right child that has a left child
                # Case 1: No right child
                if current.right is None:
                    if parent is None:
                        self.root = current.left
                    else:
                        # if parent > current value, make current left child of a child of parent
                        if current.value < parent.value:
                            parent.left = current.left
                        elif current.value > parent.value:
                            parent.right = current.left
                # Case 2: Right child which doesn't have a left child
                elif current.right.left is None:
                    if parent is None:
                        self.root = current.right
                    else:
                        if current.value < parent.value:
                            parent.left = current.right
                        elif current.value > parent.value:
                            parent.right = current.right
                # Case 3: Right child that has a left child
                else:
                    left = current.right.left
                    left_parent = current.right
                    while left.left is not None:
                        left_parent = left
                        left = left.left

                    left_parent.left = left.right
                    left.left = current.left
                    left.right = current.right

                    if parent is None:
                        self.root = left
                    else:
                        if current.value < parent.value:
                            parent.left = left
                        elif current.value > parent.value:
                            parent.right = left
                return True
        return False

    # ============ Printing ===============
    def __str__(self):
        if not self.root:
            return "<empty tree>"
        return display(self.root)


def main():
    tree = Tree(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree)
    print("Lookup: ", tree.lookup(170))
    print("Remove: ", tree.remove(20))
    print(tree)


if __name__ == '__main__':
    main()
