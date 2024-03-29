# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])
        while queue:
            total, count = 0, len(queue)
            for i in range(len(queue)):
                cur = queue.popleft()
                total += cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            ans.append(total/count)
        return ans