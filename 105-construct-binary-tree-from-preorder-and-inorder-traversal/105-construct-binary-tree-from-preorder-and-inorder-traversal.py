# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)-1
        return self.helper(0,n,0,n,preorder,inorder)
    def helper(self,prestart,preend,instart,inend,preorder,inorder):
        if prestart > preend:
            return None
        root = TreeNode(preorder[prestart])
        idx = inorder.index(root.val)
        diff = idx - instart
        root.left = self.helper(prestart+1, prestart+diff, instart,idx-1,preorder,inorder)
        root.right = self.helper(prestart+diff+1,preend,idx+1,inend,preorder,inorder)
        
        return root