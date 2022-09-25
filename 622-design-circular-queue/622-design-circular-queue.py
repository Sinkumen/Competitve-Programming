class Node:
    def __init__(self,val=-1):
        self.val = val
        self.next = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.curSize = 0
        self.size = k
        self.head = Node()
        self.tail = self.head


    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail.next = Node(value) 
            self.tail = self.tail.next
            self.curSize += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        nxt = self.head.next
        self.head.next = nxt.next 
        if not self.head.next:
            self.tail = self.head
        self.curSize -= 1
        return True
       

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val 
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val 

    def isEmpty(self) -> bool:
        return self.curSize == 0
        

    def isFull(self) -> bool:
        return self.curSize == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()