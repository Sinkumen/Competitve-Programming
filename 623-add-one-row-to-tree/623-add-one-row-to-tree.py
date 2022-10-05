# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node,d):
            if d == depth-1:
                l = TreeNode(val)
                l.left = node.left
                node.left = l
                
                r = TreeNode(val)
                r.right = node.right
                node.right = r
                return
            if node.left: dfs(node.left,d+1)
            if node.right: dfs(node.right,d+1)
        temp = TreeNode(-1,root)
        dfs(temp,0)
        return temp.left