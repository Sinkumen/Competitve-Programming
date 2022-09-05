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
            temp = []
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                temp.append(cur.val)
                for nxt in cur.children:
                    queue.append(nxt)
            ans.append(temp)
        return ans
            
            