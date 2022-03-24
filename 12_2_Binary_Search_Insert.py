class Node():
    def __init__(self,data):
        self.data = data
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def set_root(self,data):
        self.root = Node(data)

    def find(self,data):
        if self.find_node_by_data(self.root,data) == False:
            return False
        else:
            return True
    
    def find_node_by_data(self,current_node,data):
        if current_node == None:
            return False
        print(current_node.data)
        if data == current_node.data:
            return current_node
        
        if data < current_node.data:
            return self.find_node_by_data(current_node.left, data)
        
        if data > current_node.data:
            return self.find_node_by_data(current_node.right, data)

def temp_data_insert(root):
    node_2 = Node(3)
    node_3 = Node(10)
    root.left = node_2
    root.right = node_3

    node_4 = Node(1)
    node_5 = Node(5)
    node_2.left = node_4
    node_2.right = node_5

    node_6 = Node(8)
    node_3.left = node_6

BST = BinarySearchTree()
BST.set_root(7)
BST.root = temp_data_insert(BST.root)
BST.find(5)
print(BST)
