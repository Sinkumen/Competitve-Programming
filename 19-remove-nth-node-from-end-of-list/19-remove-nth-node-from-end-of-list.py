# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findLength(node):
            if not node: return 0
            return findLength(node.next) + 1
        size = findLength(head)
        ans = ListNode()
        ans.next = head
        cur = ans.next
        prev = ans
        curSize = 1
        while curSize < (size - n) + 1:
            curSize += 1
            prev = cur
            cur = cur.next
        if prev:
            prev.next = cur.next
            return ans.next
        return 
        