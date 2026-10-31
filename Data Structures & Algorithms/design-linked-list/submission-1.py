class DoublyLinkListNode:
    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = DoublyLinkListNode()
        self.tail = DoublyLinkListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        

    def get(self, index: int) -> int:
        if not (0 <= index <= self.length - 1):
            return -1

        i = 0
        curr = self.head

        while i < index:
            curr = curr.next
            i += 1

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        node = DoublyLinkListNode(val=val)

        if self.length == 0:
            self.head = node
            self.tail = self.head
            self.length += 1
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = self.head.prev
        self.length += 1


    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            return
        
        node = DoublyLinkListNode(val=val)

        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        self.length += 1       
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index > self.length - 1:
            return

        i = 0
        curr = self.head

        while i < index:
            curr = curr.next
            i += 1

        node = DoublyLinkListNode(val=val)
        curr.prev.next = node
        node.prev = curr.prev
        node.next = curr
        curr.prev = node

        self.length += 1      


    def deleteAtIndex(self, index: int) -> None:
        if not (0 <= index <= self.length - 1):
            return

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return

        i = 0
        curr = self.head

        while i < index:
            curr = curr.next
            i += 1
        
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)