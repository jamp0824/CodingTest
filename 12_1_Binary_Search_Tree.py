class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self,data):
        self.root = Node(data)

BST = BinarySearchTree()
BST.set_root(1)

print(BST.root.data)
        