# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        cur = head
        prev = head
        pos = 1
        cnt = 1
        lst = head
        while right >= cnt:
            prev = prev.next
            cnt += 1
        while cur:
            if left > pos:
                cur = cur.next
                pos += 1
            else:
                if right >= pos:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                    pos += 1 
                else:
                    break
        if left == 1:
            return prev
        cnt = 1        
        while left > cnt+1:
            lst = lst.next
            cnt += 1

        lst.next = prev
        return head
                
        