# Program to invert a Binary Tree

# A class to store a binary stree
class Node:
    def __init__(self, data , left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
# Function to perform preorder traversal on a give

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# Utility function swap left subtree with right subrree

def swap(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = root.left


# Function to invert a given binary tree

def invertBinaryTree(root):
    if root is None:
        return
    swap(root)

    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(root.left.data, root.right.data)

    invertBinaryTree(root)
    preorder(root)