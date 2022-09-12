# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        res = str(root.val)
        if left:
            res += f"({left})"
        elif right:
            res += f"()"
        if right:
            res += f"({right})"
        return res