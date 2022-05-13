"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = deque([root])
        prev = None
        while queue:
            size = len(queue)
            for i in range(size-2,-1,-1):
                queue[i].next = queue[i+1]
            for i in range(size):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root