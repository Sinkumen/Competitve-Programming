# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        last = head
        count = 1
        while last.next:
            count += 1
            last = last.next
            
        k = k%count
        
        for i in range(k):
            last = head
            prev = None
            count = 1
            while last.next:
                count += 1
                prev = last
                last = last.next
            prev.next = None
            last.next = head
            head = last
            
        return head
        
            