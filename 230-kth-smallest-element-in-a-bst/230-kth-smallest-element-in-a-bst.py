# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = deque()
        self.inOrderTraversal(root,res)
    
        return res[k-1]
    
    def inOrderTraversal(self,node,res):
        if not node: return
        self.inOrderTraversal(node.left,res)
        res.append(node.val)
        self.inOrderTraversal(node.right,res)
            
        