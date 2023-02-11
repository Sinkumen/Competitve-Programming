class ListNode:
    def __init__(self,val,nxt = None,prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.key = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.nodes = defaultdict()
        self.list = ListNode("root")
        self.tail = self.list
        

    def get(self, key: int) -> int:
        # print([(key,val.val) for key,val in self.nodes.items()],key)
        if key in self.nodes:
            cur = self.nodes[key]
            prev = cur.prev
            nxt = cur.next
            
            if nxt:
                nxt.prev = prev
                prev.next = nxt
                cur.next = None
                cur.prev = self.tail
                self.tail.next = cur
                self.tail = self.tail.next
            # print(self.list.next.val,prev.val,"last")
            return cur.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print([(key,val.val) for key,val in self.nodes.items()],key)
        while self.size and self.size >= self.capacity:
            if self.size == self.capacity and key in self.nodes:
                break
            # print("fg")
            # print(self.list.next.val)
            k = self.list.next.key
            if self.list.next.next:
                self.list.next.next.prev = self.list
            self.list.next = self.list.next.next
            self.size -= 1
            del self.nodes[k]
            if not self.list.next:
                self.tail = self.list
            
        if self.size <= self.capacity:
            if key in self.nodes:
                cur = self.nodes[key]
                cur.val = value
                # print(cur.val,key)
                prev = cur.prev
                nxt = cur.next
                if nxt:
                    nxt.prev = prev
                    prev.next = nxt
                    cur.next = None
                    cur.prev = self.tail
                    self.tail.next = cur
                    self.tail = self.tail.next
            else:
                cur = ListNode(value)
                cur.key = key
                cur.prev = self.tail
                self.tail.next = cur
                self.tail = self.tail.next
                # print(self.list.next.val)
                self.nodes[key] = cur
                self.size += 1
                
                
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)