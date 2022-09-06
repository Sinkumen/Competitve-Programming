# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0
            one = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None
                
            if one or left or right:
                return 1
            return 0
        cur = dfs(root)
        return root if cur else None
            