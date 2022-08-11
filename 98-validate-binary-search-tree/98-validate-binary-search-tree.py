# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(upper,lower,node):
            if lower >= node.val or node.val >= upper:
                return False
            left = True
            right = True
            if node.left:
                left = dfs(node.val,lower,node.left)
            if node.right:
                right = dfs(upper,node.val,node.right)
            return left & right
        
        return dfs(float("inf"),float("-inf"),root)