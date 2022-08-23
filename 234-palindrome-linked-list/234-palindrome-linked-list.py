# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        half = length//2
        
        hnode = head
        count = 0
        while hnode:
            count += 1
            if count == half:
                nxt = hnode.next
                hnode.next = None
                hnode = nxt
                break
            hnode = hnode.next
            
        prev = None
        cur = hnode
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        first = head
        second = prev
        mismatch = 0
        while first or second:
            if first and second:
                if first.val != second.val:
                    return False
                first = first.next
                second = second.next
            elif first:
                mismatch += 1
                first = first.next
            else:
                mismatch += 1
                second = second.next
        
        return mismatch <= 1    
