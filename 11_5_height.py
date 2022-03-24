class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to calculate the height of a given binary tree
def height(root):
 
    # base case: empty tree has a height of 0
    if root is None:
        return 0
 
    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))
 
 
if __name__ == '__main__':
 
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
 
    print('The height of the binary tree is', height(root))