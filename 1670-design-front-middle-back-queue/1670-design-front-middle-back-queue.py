class Node:
    def __init__(self,val = 0):
        self.val = val
        self.next = None
        self.prev = None
class FrontMiddleBackQueue:

    def __init__(self):
        self.size = 0
        self.head = Node()
        self.tail = self.head

    def pushFront(self, val: int) -> None:
        first = self.head.next
        new = Node(val)
        new.prev = self.head
        new.next = first
        self.head.next = new
        if first:
            first.prev = new
        else:
            self.tail = self.head.next
            
        self.size += 1
            

    def pushMiddle(self, val: int) -> None:
        mid = self.size//2
        count = 0
        cur = self.head
        while cur and count < mid:
            cur = cur.next
            count += 1
        nxt = cur.next
        new = Node(val)
        new.prev = cur
        new.next = nxt
        cur.next = new
        if nxt: 
            nxt.prev = new
        else:
            self.tail = cur.next
        self.size += 1
        
            

    def pushBack(self, val: int) -> None:
        prev = self.tail
        new = Node(val)
        new.prev = prev
        self.tail.next = new
        self.tail = self.tail.next
        self.size += 1

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        first = self.head.next
        second = first.next
        if second:
            self.head.next = second
            second.prev = self.head
        else:
            self.head.next = None
            self.tail = self.head
        self.size -= 1
        return first.val
        

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1
        
        mid = self.size//2 if self.size%2==0 else self.size//2+1
        count = 0
        cur = self.head
        while cur and count < mid:
            cur = cur.next
            count += 1
        prev = cur.prev
        nxt = cur.next
        prev.next = nxt
        if nxt: 
            nxt.prev = prev
        else:
            self.tail = prev
        self.size -= 1
        return cur.val

    def popBack(self) -> int:
        if self.size == 0:
            return -1
        
        cur = self.tail.val
        prev = self.tail.prev
        prev.next = None
        self.tail = prev
        self.size -= 1
        return cur
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()