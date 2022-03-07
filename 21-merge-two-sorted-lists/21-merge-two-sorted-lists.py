# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        ans = ListNode(0)
        cur = ans
        while first or second:
            if not first:
                cur.next = second
                break
            if not second:
                cur.next = first
                break
                
            if first.val <= second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second  = second.next
    
            cur = cur.next
                
        return ans.next