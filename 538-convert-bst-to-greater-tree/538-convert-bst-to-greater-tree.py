# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,fromRight):
            if not node:
                return fromRight
            right = dfs(node.right,fromRight)
            node.val += right
            left = dfs(node.left,node.val)
            return left
        dfs(root,0)
        return root