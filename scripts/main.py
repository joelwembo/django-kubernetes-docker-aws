# class Node:
#     def __init__(self, value, key=None, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#         self.key = key
#
#
#     def printTree(self):
#         if self.left:
#             self.left.printTree
#         print(self.value, end=' ')
#
#         if self.right:
#             self.right.printTree
#
#
#
#     def insert(self, value):
#         if value < self.value:
#             if self.left is None:
#                 self.left = Node(value)
#             else:
#                 self.left.insert(value)
#         else:
#             if self.right is None:
#                 self.right = Node(value)
#             else:
#                 self.right.insert(value)
#
#     def inorder_traversal(self):
#         if self.left:
#             self.left.inorder_traversal()
#         print(self.value)
#
#         if self.right:
#             self.right.inorder_traversal()
#
#     def preorder_traversal(self):
#         print(self.value)
#         if self.left:
#             self.left.inorder_traversal()
#         if self.right:
#             self.right.inorder_traversal()
#
#     def postorder_traversal(self):
#         if self.left:
#             self.left.postorder_traversal()
#         if self.right:
#             self.right.postorder_traversal()
#         print(self.value)
#
#     def find(self, value):
#         if value < self.value:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.find(value)
#         elif value > self.value:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.find(value)
#
#         return True
#
# def inorder(node, list):
#     if node is None:
#         return
#     inorder(node.left, list)
#     list.append(node.value)
#     inorder(node.right, list)
#
# def postnorder(node, list):
#     if node is None:
#         return
#     postnorder(node.left, list)
#     postnorder(node.right, list)
#     list.append(node.value)
#
# def is_subList(x , y):
#     for i in range(len(x) - len(y) +1):
#         if x[i: i + len(y)] == y:
#             return True
#         return False
#
#
# def checkSubTree(tree, subtree):
#     if tree == subtree:
#         return True
#     if tree is None:
#         return False
#
#     first = []
#     second = []
#     inorder(tree, first)
#     inorder(subtree, second)
#
#     if not is_subList(first, second):
#         return False
#     first.clear()
#     second.clear()
#
#     postnorder(tree, first)
#     postnorder(subtree, second)
#
#     if not is_subList(first, second):
#         return False
#
#     return True



def ConvertNumberToRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]

    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]

    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i] , end = '')
            div -= 1
        i = 1

def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num

def most_frequent_char(string):
    test_string = string

    all_freq = {}
    for i in test_string:
        if i in all_freq:
            all_freq[i] = +1
        else:
            all_freq[i] = 1

    return max(all_freq, key = all_freq.get)

if __name__ == "__main__":
    # testing int to roman:
    # number1 = 36500
    # print("the Romain value is : ", end=" ")
    # ConvertNumberToRoman(number1)

    # List = [2, 1, 2, 2, 1, 3]
    # print(most_frequent(List))
    print(most_frequent_char("fabriceotepaaaaaa"))









