# BFS traversal function.
# Usually would be a method of the Tree class, but kept standalone for clarity.
from Code.Trees.CustomBinaryTree import Tree


def breath_first_search(tree: Tree):  # TC: O(n) SC: O(n)
    """
        Perform BFS on a binary tree and return a list of node values in level-order.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    current_node = tree.root  # we start with the root node
    lst = []  # we insert numbers into this list in the order of BST
    q = [current_node]  # queue for BFS traversal; can grow large for big trees

    while len(q) > 0:
        current_node = q.pop(0)
        lst.append(current_node.value)
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)
    return lst


def breath_first_search_recursive(tree: Tree, q=None, lst=None):  # TC: O(n) SC: O(n)
    if q is None:
        q = [tree.root]
    if lst is None:
        lst = []

    # End case if queue is empty
    if not q:
        return lst

    current_node = q.pop(0)
    lst.append(current_node.value)
    if current_node.left:
        q.append(current_node.left)
    if current_node.right:
        q.append(current_node.right)

    return breath_first_search_recursive(tree, q, lst)


#       9
#   4       20
# 1    6  15     170
def main():
    tree = Tree(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree)
    print('iterative: ', breath_first_search(tree))
    print('recursive: ', breath_first_search_recursive(tree))


if __name__ == '__main__':
    main()
