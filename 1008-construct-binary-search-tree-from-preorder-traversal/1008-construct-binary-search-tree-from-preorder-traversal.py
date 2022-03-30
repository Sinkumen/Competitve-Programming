# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(parent,val):
            if not parent:
                return TreeNode(val)
            if parent.val > val:
                parent.left = build(parent.left,val)
            else:
                parent.right = build(parent.right,val)
            return parent
        
        root = None
        for n in preorder:
            root = build(root,n)
            
        return root