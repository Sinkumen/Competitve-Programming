# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        ans = ListNode()
        prev = ans
        cur = head
        count = 1
        while cur:
            if cur.next and cur.val == cur.next.val:
                count += 1
                cur = cur.next
            else:
                if count == 1:
                    temp = cur
                    prev.next = ListNode(cur.val)
                    prev = prev.next 
                cur = cur.next
                count = 1
        return ans.next
            
                