# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def makeGreater(node,summ):
            if not node:
                return summ
            right = makeGreater(node.right,summ)
            node.val += (right)
            left = makeGreater(node.left, node.val)
            
            return left
        makeGreater(root,0)
        return root
            
            