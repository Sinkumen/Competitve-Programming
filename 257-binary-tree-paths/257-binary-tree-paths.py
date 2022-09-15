# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node,res):
            if not node.left and not node.right:
                res.append(str(node.val))
                ans.append("->".join(res))
                res.pop()
            res.append(str(node.val))
            if node.left: dfs(node.left,res)
            if node.right: dfs(node.right,res)
            res.pop()
        dfs(root,[])
        return ans
            
          
            