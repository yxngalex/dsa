# DFS traversal function.
# (Same as BFS) Usually would be a method of the Tree class, but kept standalone for clarity.
from Trees.CustomBinaryTree import Tree


# In-order: [1, 4, 6, 9, 15, 20, 170]
def in_order_depth_first_search(tree: Tree):  # TC: O(n) SC: O(h)  h being height of the tree
    return in_order(tree.root, [])


# Pre-order: [9, 4, 1, 6, 20, 15, 170]
def pre_order_depth_first_search(tree: Tree):  # TC: O(n) SC: O(h)
    return pre_order(tree.root, [])


# Post-order: [1, 6, 4, 15, 170, 20, 9]
def post_order_depth_first_search(tree: Tree):  # TC: O(n) SC: O(h)
    return post_order(tree.root, [])


def in_order(node, lst):
    print(node.value)
    if node.left:
        in_order(node.left, lst)
    lst.append(node.value)
    if node.right:
        in_order(node.right, lst)
    return lst


def pre_order(node, lst):
    print(node.value)
    lst.append(node.value)
    if node.left:
        pre_order(node.left, lst)
    if node.right:
        pre_order(node.right, lst)
    return lst

def post_order(node, lst):
    print(node.value)
    if node.left:
        post_order(node.left, lst)
    if node.right:
        post_order(node.right, lst)
    lst.append(node.value)
    return lst

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
    print('In Order DFS: ', in_order_depth_first_search(tree))
    print('Pre Order DFS: ', pre_order_depth_first_search(tree))
    print('Post Order DFS: ', post_order_depth_first_search(tree))


if __name__ == '__main__':
    main()
