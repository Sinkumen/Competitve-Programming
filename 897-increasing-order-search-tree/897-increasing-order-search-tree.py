# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(node,res):
            if not node:
                return
            inOrder(node.left,res)
            res.append(node.val)
            inOrder(node.right,res)
            
        res = []
        inOrder(root,res)
        ans = TreeNode(res[0])
        new = ans
        for i in range(1,len(res)):
            new.right = TreeNode(res[i])
            new = new.right
        return ans