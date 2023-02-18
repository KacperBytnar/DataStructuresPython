# Define the LinkedListNode class with a constructor that 
# initializes the value and the next node pointer.
class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
        
# Define the LinkedList class with a constructor that initializes the head node.
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    # Insert a new node with the given value at the end of the linked list.
    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None: # if the linked list is empty
            self.head = node # set the new node as the head
            return 
        
        currentNode = self.head
        while(True):
            if currentNode.nextNode is None:
                currentNode.nextNode = node 
                break
            currentNode = currentNode.nextNode
    
    # Print the values of all the nodes in the linked list.
    def printLinkedList(self):
        currentNode=self.head
        while currentNode is not None:
            print (currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")


ll = LinkedList()
ll.printLinkedList()
ll.insert(3)
ll.printLinkedList()
ll.insert(61)
ll.printLinkedList()
ll.insert(11)
ll.printLinkedList()