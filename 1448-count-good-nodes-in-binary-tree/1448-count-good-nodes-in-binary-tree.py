# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,upper):
            if not node: return 0
            ans = 0
            if node.val >= upper:
                ans += 1
            ans += dfs(node.left,max(node.val,upper))
            ans += dfs(node.right,max(node.val,upper))
            return ans
        
        return dfs(root,root.val)