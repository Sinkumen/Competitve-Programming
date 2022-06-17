# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return not node.left and not node.right
        @lru_cache(None)
        def dfs(node,install):
            if isLeaf(node):
                if install == 0 or install == 2:
                    return 1
                else:
                    return 0
            if install == 0:
                res = 1
                if node.left:
                    res += min(dfs(node.left,1),dfs(node.left,0))
                if node.right:
                    res += min(dfs(node.right,1),dfs(node.right,0))
                return res
            elif install == 2:
                if node.left and node.right:
                    both = dfs(node.left,0) + dfs(node.right,0)
                    right = dfs(node.left,0) + dfs(node.right,2)
                    left = dfs(node.left,2) + dfs(node.right,0)
                    return min(both,right,left)
                elif node.right:
                    return dfs(node.right,0)
                elif node.left:
                    return dfs(node.left,0)
            else:
                res = 0
                if node.left :
                    res += min(dfs(node.left,2),dfs(node.left,0))
                if node.right:
                    res += min(dfs(node.right,2),dfs(node.right,0))
                return res
        if isLeaf(root):
            return 1
        start = TreeNode()
        start.left = root 
        return dfs(start,1)
  
            
            
            