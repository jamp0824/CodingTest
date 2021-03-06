# Recursive Python program for level
# order traversal of Binary Tree
 
# A node structure
 
 
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def height(root):
 
    # base case: empty tree has a height of 0
    if root is None:
        return 0
 
    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))

# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
 
 
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
 
 
# Driver program to test above function
root = Node(7)
node_3 = Node(3)
node_10 = Node(10)
root.left = node_3
root.right = node_10

node_1 = Node(1)
node_5 = Node(5)
node_3.left = node_1
node_3.right = node_5

node_8 = Node(8)
node_10.left = node_8

node_4 = Node(4)
node_5.left = node_4
    
node_12 = Node(12)
node_4.left = node_12
 
print("Level order traversal of binary tree is -")
printLevelOrder(root)
print()
print('The height of the binary tree is', height(root))
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)