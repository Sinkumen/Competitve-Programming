# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        carry = 0
        ans = ListNode()
        res = ans
        while first or second:
            cur = carry 
            if first:
                cur += first.val
                first = first.next
            if second:
                cur += second.val
                second = second.next
            if cur >= 10:
                carry = 1
                res.next = ListNode(cur%10)
                res = res.next
            else:
                carry = 0
                res.next = ListNode(cur)
                res = res.next
        if carry:
            res.next = ListNode(carry)
        return ans.next