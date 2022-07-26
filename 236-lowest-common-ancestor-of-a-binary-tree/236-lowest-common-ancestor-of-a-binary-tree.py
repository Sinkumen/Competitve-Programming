# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(node,p,q)[0]
    def dfs(self,node,p,q):
        if not node.left and not node.right:
            if node.val == q.val or node.val == p.val:
                return (node,1)
            else:
                return (node,0)
            
        left = (0,0)
        right = (0,0)
        
        if node.left:
            left = self.dfs(node.left,p,q)
        if node.right:
            right =  self.dfs(node.right,p,q)
        
        if left[1] == 1 and right[1] == 1:
            return (node,2)
        
        if left[1] == 2:
            return left
        if right[1] == 2:
            return right
        # print(node.val,left[0].val,right[0].val)
        if node.val == q.val or node.val == p.val:
            # print(node.val,left[0].val,right[0].val)
            if left[1] == 1 or right[1] == 1:
                return (node,2)
            else:
                return (node,1)
        if left[1] == 1 or right[1] == 1:
            return (node,1)
        return (node,0)