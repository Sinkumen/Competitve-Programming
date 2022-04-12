# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findSize(node):
            if not node:
                return 0
            return findSize(node.next) + 1
        size = findSize(head)
        first = head
        last = head
        cur = head
        curSize = 1
        while cur:
            if curSize < k:
                first = cur.next
            if size - curSize + 1 == k:
                last = cur
            cur = cur.next
            curSize += 1
        first.val, last.val = last.val, first.val
        return head
            
        