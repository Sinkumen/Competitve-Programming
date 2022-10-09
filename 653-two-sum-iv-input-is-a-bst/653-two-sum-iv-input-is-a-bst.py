# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque([root])
        visited = set()
        while queue:
            cur = queue.popleft()
            if k - cur.val in visited: return True
            visited.add(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return False