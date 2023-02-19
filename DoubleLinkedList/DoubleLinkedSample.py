class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
            
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.next = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index>0:
            cur=cur.next
            index -= 1
        
        if cur and cur != self.right and index ==0:
            return cur.val
        return -1

    #def addAtHead(self, val: int) -> None:
        

    #def addAtTail(self, val: int) -> None:
        

    #def addAtIndex(self, index: int, val: int) -> None:
        

    #def deleteAtIndex(self, index: int) -> None:


dll = MyLinkedList()
dll.next = ListNode(1)
dll.next = ListNode(5)
dll.
dll.get(1)