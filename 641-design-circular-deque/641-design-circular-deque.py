class Node:
    def __init__(self,val = -1):
        self.val = val
        self.next = None
        self.prev = None
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.curSize = 0
        self.head = Node()
        self.tail = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        nxt = self.head.next
        new = Node(value)
        new.prev = self.head
        new.next = nxt
        if nxt: nxt.prev = new
        self.head.next = new
        if self.isEmpty():
            self.tail = self.head.next
        self.curSize += 1
        return True
        


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        prev = self.tail
        new = Node(value)
        new.prev = prev
        self.tail.next = new
        self.tail = self.tail.next
        self.curSize += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        first = self.head.next
        self.head.next = first.next
        if not self.head.next:
            self.tail = self.head
        else:
            self.head.next.prev = self.head
        self.curSize -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        prev = self.tail.prev
        prev.next = None
        self.tail = prev
        self.curSize -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()