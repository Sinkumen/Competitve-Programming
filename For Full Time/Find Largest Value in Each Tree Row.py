# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            s = len(queue)
            maxx = float('-inf')
            for i in range(s):
                node = queue.popleft()
                maxx = node.val if node.val>maxx else maxx
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(maxx)
        return ans
                