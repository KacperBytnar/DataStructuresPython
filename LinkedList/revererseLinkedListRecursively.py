#Define  class called Solution that will hold the reverseList function
class Solution:
    # Define the reverseList function that takes a LinkedListNode as input and returns a LinkedList
    def reverseList(self, head: LinkedListNode) -> LinkedList:
        # recursive T: O(n) M: O(n)
        if not head:
            return None

        newHead = head
        if head.nextNode:
            newHead = self.reverseList(head.nextNode)
            head.nextNode.nextNode = head
        head.nextNode = None
        
        return newHead

# Create a linked list called ll and insert the values [1,2,3,4,5] into it
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
# Print the original linked list
ll.printLinkedList()

sol = Solution()
# Call the reverseList function from the Solution class with the head of the linked list as input
node = sol.reverseList(ll.head)

# Print the reversed linked list by iterating over the nodes in the reversed list and printing their values
while node:
    print(node.value, end=' ')
    node = node.nextNode

