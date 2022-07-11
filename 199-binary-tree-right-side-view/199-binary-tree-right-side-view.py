# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            queue = deque([root])
            ans = []
            while queue:
                ans.append(queue[-1].val)
                for _ in range(len(queue)):
                    top = queue.popleft()
                    if top.left:
                        queue.append(top.left)
                    if top.right:
                        queue.append(top.right)
            return ans
                
        