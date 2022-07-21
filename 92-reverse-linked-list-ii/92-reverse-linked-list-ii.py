# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        prev = None
        count = 1
        while cur and count < left:
            prev = cur
            cur = cur.next
            count += 1
        
        tempPrev = None
        tempCur = cur
        last = None
        while tempCur and left <= right:
            if left == right:
                last = tempCur.next
                tempCur.next = tempPrev
                tempPrev = tempCur
                left += 1
            else:
                nxt = tempCur.next
                tempCur.next = tempPrev
                tempPrev = tempCur
                tempCur = nxt
                left += 1
        cur.next = last
        if prev:
            prev.next = tempCur
            return head
        return tempPrev
        
        
        print(cur.val,prev.val)
    