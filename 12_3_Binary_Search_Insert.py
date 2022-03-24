
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, data):
        self.root = Node(data)

    def find(self, data):
        if self.find_node_by_recursion(self.root, data) == False:
            return False
        else:
            return True

    def find_node_by_recursion(self, current_node, data):
        if current_node == None:
            return False
        if data == current_node.data:
            return current_node

        if data < current_node.data:
            return self.find_node_by_recursion(current_node.left, data)
        if data > current_node.data:
            return self.find_node_by_recursion(current_node.right, data)

    def insert(self, data):
        if self.root == None:
            self.set_root(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, current_node, data):
        if data == current_node.data:
            print(f"이미 {data}값이 존재합니다. 중복된 값은 삽입할 수 없습니다.")
            return
        if data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
            else:
                self.insert_node(current_node.left, data)

        elif data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
            else:
                self.insert_node(current_node.right, data)

BST = BinarySearchTree()
BST.set_root(7)

BST.insert(3)
BST.insert(1)
BST.insert(5)
BST.insert(10)
BST.insert(8)

print("root -> left -> left : ", BST.root.left.left.data)
print("root -> left -> right : ", BST.root.left.right.data)
print("root -> right -> left : ", BST.root.right.left.data)

BST.insert(4)
BST.insert(12)
BST.insert(15)

print("root -> right -> right : ", BST.root.right.right.data)
print("root -> right -> right -> right : ", BST.root.right.right.right.data)