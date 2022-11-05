# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def __repr__(self, key):
        return str(key)

# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)



# Binary search in python

def binarySearch(array , x , low, high):

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Driver code
if __name__ == "__main__":
     # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # "Preorder traversal of binary tree is"
    # printPreorder(root + "left left : " + root.left.left)
     array = [3, 4, 5, 6, 7, 8, 9]
     x = 4
     print(binarySearch(array,4, len(array) -1 ))
