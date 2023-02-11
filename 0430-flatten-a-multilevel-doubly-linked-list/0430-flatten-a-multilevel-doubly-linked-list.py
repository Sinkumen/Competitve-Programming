"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            if not node:
                return 
            if not node.next and not node.child:
                return node
            
            nxt = helper(node.next)
            child = helper(node.child)
            if child:

                if node.next:
                    node.next.prev = child
                child.next = node.next
                node.child.prev = node 
                node.next = node.child
            node.child = None

            return nxt if nxt else child
        helper(head)
        return head
        