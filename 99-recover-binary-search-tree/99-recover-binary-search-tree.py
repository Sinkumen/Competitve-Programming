# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        swap = {}
        def dfs(node):
            if not node:
                return
    
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)
        dfs(root)
        srtd = sorted(n.val for n in inorder)
        
        for i in range(len(srtd)):
            inorder[i].val = srtd[i]

        