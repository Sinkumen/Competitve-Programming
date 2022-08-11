# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(upper,lower,node):
            if not node:
                return True
            if lower >= node.val or node.val >= upper:
                return False
            
            return dfs(node.val,lower,node.left) & dfs(upper,node.val,node.right)
           
        
        return dfs(float("inf"),float("-inf"),root)