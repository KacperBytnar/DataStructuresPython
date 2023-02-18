#Define  class called Solution that will hold the reverseList function
class Solution:
    # Define the reverseList function that takes a LinkedListNode as input and returns a LinkedList
    def reverseList(head: LinkedListNode) -> LinkedList:
        # Initialize two variables prev and curr to None and head respectively
        prev, curr = None, head

        # Enter a while loop that will continue until curr is not None
        while curr:
            # Initialize a variable nxt to the next node in the list following curr
            nxt = curr.nextNode
            # Set the nextNode of curr to prev, effectively reversing the nextNode pointer of the current node
            curr.nextNode = prev
            # Update prev to curr
            prev = curr
            # Update curr to nxt
            curr = nxt
        # Return prev, which is the new head of the reversed list
        return prev

# Create a linked list called ll and insert the values [1,2,3,4,5] into it
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
# Print the original linked list
ll.printLinkedList()

# Call the reverseList function from the Solution class with the head of the linked list as input
node = Solution.reverseList(ll.head)

# Print the reversed linked list by iterating over the nodes in the reversed list and printing their values
while node:
    print(node.value, end=' ')
    node = node.nextNode
