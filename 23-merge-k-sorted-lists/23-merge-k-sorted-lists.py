# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            if lists[0]:
                return lists[0]
            return 
        mid = ceil(len(lists)/2)
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        l = left
        r = right
        ans = ListNode()
        res = ans
        while l and r :
            if l.val < r.val:
                res.next = l
                res = res.next
                l = l.next
            else:
                res.next = r
                res = res.next
                r = r.next
        if r:res.next = r
        if l:res.next = l
        
        return ans.next