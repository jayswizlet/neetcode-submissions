class ListNode:
    def __init__(self, val, next_node=None):
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
            i += 1
            curr = curr.next
        return -1
            
        
    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode 
        if not newNode.next:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.tail:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        # curr = self.head
        # if index == 0 or curr == None:
        #     return False
        # for i in range(index):
        #     if curr.next == None:
        #         return False
        #     curr = curr.next
        #     if curr.next is not None and curr.next.next is not None:
        #         if i == index - 1:
        #             curr.next = curr.next.next
        #             self.head = curr
        #             return True
        # return False
        # if index == 0:
        #     if self.head == None:
        #         return False
        #     self.head = self.head.next
        #     return True
        # curr = self.head
        # for i in range(index - 1):
        #     if curr is None or curr.next is None:
        #         return False
        #     curr = curr.next
        # if curr.next == None:
        #     return False
        # curr.next = curr.next.next
        # return True

        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        curr = self.head
        for i in range(index-1):
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
        curr = self.head
        nodeList = []
        while curr:
            nodeList.append(curr.val)
            curr = curr.next
        return nodeList
