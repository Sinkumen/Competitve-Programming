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
            if node.val in swap:
                node.val = swap[node.val]
                
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        dfs(root)
        srtd = sorted(inorder)
        swap = {}
        for i in range(len(srtd)):
            if srtd[i] != inorder[i]:
                swap[inorder[i]] = srtd[i]
        dfs(root)
        