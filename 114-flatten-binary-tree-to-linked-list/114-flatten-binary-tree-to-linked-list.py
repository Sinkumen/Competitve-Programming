# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def join(left,right):
            cur = left
            while cur.right:
                cur = cur.right
            cur.right = right
        def dfs(node):
            if not node:
                return 
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left:
                join(left,right)
                node.left = None
                node.right = left
            return node
        dfs(root)
                
            
            
            
        