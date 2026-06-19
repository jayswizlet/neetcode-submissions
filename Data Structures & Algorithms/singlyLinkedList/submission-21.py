class ListNode():
    def __init__(self,val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            if curr == None:
                return -1
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        insertNode = ListNode(val)
        if not self.head:
            self.head = insertNode
            self.tail = self.head
        else:
            insertNode.next = self.head
            self.head = insertNode
        
        

    def insertTail(self, val: int) -> None:
        insertNode = ListNode(val)
        if not self.head:
            self.head = insertNode
            self.tail = self.head
        else:
            self.tail.next = insertNode
            self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        curr = self.head
        for i in range(index - 1):
            if curr is None or curr.next is None:
                return False
            curr = curr.next
        if curr.next is None:
            return False
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        return True


    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
        
