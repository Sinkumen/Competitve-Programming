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
        last.next = head  
        k = count -  k%count
        while k:
            last = last.next
            k -= 1
        ans = last.next
        last.next = None
        
        return ans
        
            