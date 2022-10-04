# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Do a heap from the lists O(nlog(n))
        heap = []
        for linkedList in lists:
            while(linkedList is not None):
                heappush(heap, linkedList.val)
                linkedList = linkedList.next

        if not heap:
            return None
            
        # Then create a linked list O(n)
        head = ListNode(heappop(heap))
        node = head
        while(heap):
            nextElt = heappop(heap)
            node.next = ListNode(nextElt)
            node = node.next
        return head