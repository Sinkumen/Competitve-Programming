# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        great = ListNode()
        l = less
        g = great
        cur = head
        while cur:
            if cur.val < x:
                l.next = ListNode(cur.val)
                l = l.next
            else:
                g.next = ListNode(cur.val)
                g = g.next
            cur = cur.next

        l.next = great.next
        return less.next
        