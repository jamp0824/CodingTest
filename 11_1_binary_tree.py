from dataclasses import dataclass
from platform import node


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
node_2 = Node(2)
node_3 = Node(3)
root.left = node_2
root.right = node_3

node_4 = Node(4)
node_5 = Node(5)
node_2.left = node_4
node_2.right = node_5

print("루트 노드:", root.data)
print("루트 노드의 자식: ", root.left.data,root.right.data)
print("루트 노드 왼쪽 자식의 자식들:",root.left.left.data, root.left.right.data)