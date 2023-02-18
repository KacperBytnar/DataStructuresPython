class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
        
# "3" -> "7" -> "10"
        
node1 = LinkedListNode("3") # "3"
node2 = LinkedListNode("7") # "7"
node3 = LinkedListNode("10") # "10"
node4 = LinkedListNode("77") # "10"

node1.nextNode = node2 # node1 -> node2, "3" -> "7"
node2.nextNode = node3 # node2 -> node3, "7" -> "10"
node3.nextNode = node4

# node1 -> node2 -> node3

currentNode=node1

while True:
     print (currentNode.value, "->", end=" ")
     if currentNode.nextNode is None:
        print("None")
        break 
     currentNode=currentNode.nextNode