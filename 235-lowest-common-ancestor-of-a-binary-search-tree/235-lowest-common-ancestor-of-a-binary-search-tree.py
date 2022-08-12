# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        temp = p.val
        pv = min(p.val,q.val)
        qv = max(temp,q.val)
        if pv <= root.val <=  qv:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        if left:
            return left
        return self.lowestCommonAncestor(root.right,p,q)
        