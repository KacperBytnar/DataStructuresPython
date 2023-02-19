class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if(l1.value<l2.value):
                tail.nextNode = l1
                l1 = l1.nextNode      
            else:         
                tail.nextNode = l2
                l2 = l2.nextNode    

            tail=tail.nextNode
            print(tail.value)

        if l1:
            tail.nextNode=l1
        elif l2:
            tail.nextNode=l2
        
        return dummy.nextNode

# Create a linked list called ll and insert the values [1,2,3,4,5] into it
ll1 = LinkedList()
ll2 = LinkedList()
ll1.insert(1)
ll1.insert(2)
ll1.insert(4)
ll2.insert(1)
ll2.insert(3)
ll2.insert(4)

ll1.printLinkedList()
ll2.printLinkedList()
# Print the original linked list


sol = Solution()
# Call the reverseList function from the Solution class with the head of the linked list as input
node = sol.mergeTwoLists(ll1.head, ll2.head)

# Print the reversed linked list by iterating over the nodes in the reversed list and printing their values
while node:
    print(node.value, end=' ')
    node = node.nextNode

