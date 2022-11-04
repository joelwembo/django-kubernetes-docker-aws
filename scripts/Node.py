class Node:
    def __init__(self, value , key=None):
        self.value = value
        self.left = None
        self.right = None
        self.key = key

    def __repr__(self):
        return str(self.value)

    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value) # if use list (self, list) => list.append(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()


    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)

        return True

def inorder(node, list):
    if node is None:
        return
    inorder(node.left, list)
    list.append(node.value)
    inorder(node.right, list)

def postorder(node, list):
    if node is None:
        return
    postorder(node.left, list)
    postorder(node.right, list)
    list.append(node.value)


def isIdentical(x, y):
    if x is None and y is None:
        return True
    return (x is not None and y is not None) and (x.key == y.key) and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)

def is_sublist(x, y):
    for i in range(len(x) - len(y) + 1):
        if x[i: i + len(y)] == y:
            return True
        return False

def checkSubTree(tree, subtree):
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



# tree = Node(10)
# tree.insert(5)
# tree.insert(4)
# tree.insert(10)
# tree.insert(2)
# tree.insert(1)
# tree.insert(41)
# tree.insert(60)
# tree.insert(7)
# tree.insert(22)
#
# tree.preorder_traversal()
# print(tree.left.left.left.value)
#
# print(tree.find(100))
if __name__ == '__main__':

    #  # construct the first tree
    # g = Node(15)
    # x = Node(15)
    # x.left = Node(10)
    # x.right = Node(20)
    # x.left.left = Node(8)
    # x.left.right = Node(12)
    # # x.right.left = Node(16)
    # # x.right.right = Node(25)
    #
    # # construct the second tree
    # y = Node(15)
    # y.left = Node(10)
    # y.right = Node(20)
    # y.left.left = Node(8)
    # y.left.right = Node(12)
    # # y.right.left = Node(16)
    # # y.right.right = Node(25)
    #
    # if isIdentical(x, y):
    #     print('The given binary trees are identical')
    # else:
    #     print('The given binary trees are not identical')

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

    if checkSubTree(root, root.right):
        print('Yes')
    else:
        print('No')
