# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        count = 1 
        cur = head
        oddCur = odd
        evenCur = even
        while cur:
            nxt = cur.next 
            if count%2 == 0:
                evenCur.next = cur
                evenCur = evenCur.next
                evenCur.next = None
            else:
                oddCur.next = cur
                oddCur = oddCur.next
                oddCur.next = None
            cur =nxt
            count += 1
        oddCur.next = even.next
        
        return odd.next
            
            
            
        