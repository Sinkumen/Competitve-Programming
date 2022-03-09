# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        ans = ListNode(head.val)
        prev = ans
        cur = head
        while cur:
            if cur.val != prev.val:
                prev.next = ListNode(cur.val)
                prev = prev.next
            cur = cur.next
        return ans
                