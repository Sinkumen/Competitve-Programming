"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        ans = []
        while queue:
            ans.append([x.val for x in queue])
            size = len(queue)
            for _ in range(size):
                for nxt in queue.popleft().children:
                    queue.append(nxt)
        return ans
            
            