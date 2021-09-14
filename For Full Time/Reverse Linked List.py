# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head,None)
    def helper(self,cur,prev):
        if not cur: return prev
        nxt = cur.next 
        cur.next = prev
        return self.helper(nxt,cur)

     def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        