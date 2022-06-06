# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def findLen(node):
            cur = node
            length = 0
            while cur:
                length += 1
                cur = cur.next
            return length
        
        lenA = findLen(headA)
        lenB = findLen(headB)
        diff = abs(lenA-lenB)
        long = headA if lenA > lenB else headB
        short = headA if lenA <= lenB else headB
        while diff:
            long = long.next
            diff -= 1
        while long != short:
            long = long.next
            short = short.next
        return long