# for Garbage collection
import gc

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class doubly_linked_list:
    def __init__(self):
        self.head = None

#Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

#Define the method to insert the element
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

#Define the append the method to add elements at the end
    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while( last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    def deleteNode(self, dele):
         
        # Base Case
        if self.head is None or dele is None:
            return
         
        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next
 
        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev
     
        # Change prev only if node to be deleted is NOT
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele
        # Call python garbage collector
        gc.collect()

 #delete all nodes of the list
    def deleteAllNodes(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        print("All nodes are deleted successfully.")


#Print the Doubly Linked list
    def listprint(self, node):
        while(node is not None):
            print(node.data),
            last = node
            node = node.next

dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.insert(dllist.head.next,13)
dllist.append(45)
dllist.listprint(dllist.head)

dllist.deleteNode(dllist.head)
dllist.deleteNode(dllist.head.next)
dllist.deleteNode(dllist.head.next)

print("\n Modified Linked List",end=' ')
dllist.listprint(dllist.head)#delete all nodes of the list

dllist.deleteAllNodes()

#Display the content of the list
dllist.listprint(dllist.head)