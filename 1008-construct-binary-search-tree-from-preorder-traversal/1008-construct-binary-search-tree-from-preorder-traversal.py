# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(lst,lower,upper):
            if not lst or not lower <= lst[0] <= upper:
                return None
            
            cur = TreeNode(lst.pop(0))
            
            cur.left = build(lst,lower,cur.val)
            cur.right = build(lst,cur.val,upper)
            
            return cur
        return build(preorder,float("-inf"),float("inf"))