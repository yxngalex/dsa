# DFS traversal function.
# (Same as BFS) Usually would be a method of the Tree class, but kept standalone for clarity.
from Trees.CustomBinaryTree import Tree

"""
       Perform DFS on a binary tree and return a list of node values in: in-order, pre-order, post-order.

       Time Complexity: O(n)
       Space Complexity: O(H)

       H: being height of the tree

       In-order: [1, 4, 6, 9, 15, 20, 170]
       Pre-order: [9, 4, 1, 6, 20, 15, 170]
       Post-order: [1, 6, 4, 15, 170, 20, 9]
   """


def in_order_depth_first_search(tree: Tree):
    return in_order(tree.root, [])


def pre_order_depth_first_search(tree: Tree):
    return pre_order(tree.root, [])


def post_order_depth_first_search(tree: Tree):
    return post_order(tree.root, [])


def in_order(node, lst):
    if node.left:
        in_order(node.left, lst)
    lst.append(node.value)
    if node.right:
        in_order(node.right, lst)
    return lst


def pre_order(node, lst):
    lst.append(node.value)
    if node.left:
        pre_order(node.left, lst)
    if node.right:
        pre_order(node.right, lst)
    return lst


def post_order(node, lst):
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
