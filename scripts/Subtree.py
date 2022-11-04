# A class to store a binary tree node

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = right
        self.right = right

    def __repr__(self):
        return str(self.data)


def inorder(node, list):
    if node is None:
        return
    inorder(node.left, list)
    list.append(node.data)
    inorder(node.right, list)

def postorder(node, list):
    if node is None:
        return
    postorder(node.left, list)
    postorder(node.right, list)
    list.append(node.data)

def is_sublist(x, y):
    for i in range(len(x) - len(y) + 1 ):
        if x[i: i + len(y)] == y:
            return True

    return False

def checkSubtree(tree, subtree):
    if tree == subtree:
        return True

    if tree is None:
        return False

    first = []
    second = []

    inorder(tree, first)
    inorder(subtree, second)

    if not is_sublist(first, second):
        return False

    first.clear()
    second.clear()

    postorder(tree, first)
    postorder(subtree, second)

    if not is_sublist(first, second):
        return False

    return True


if __name__ == '__main__':

    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if checkSubtree(root, root.right):
        print('Yes')
    else:
        print('No')


