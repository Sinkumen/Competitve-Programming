# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
       
        start = self.dfs(root,startValue,[])
        dest = self.dfs(root,destValue,[])
		
        ans = []
        s = 0
        d = 0
        while s < len(start) and d < len(dest):
            st = start[s]
            de = dest[d]
            if st != de:
                ans = "U" * (len(start) - s) 
                ans += "".join(dest[d:])
                return ans
            s += 1
            d += 1
        if s < len(start):
            return "U"*(len(start)-s)
        elif d < len(dest):
            return "".join(dest[d:])

    def dfs(self,node,target,res):
        if not node: return None
        if node.val == target:
            return res
        res.append("L")
        left  = self.dfs(node.left,target,res)
        if left:
            return left
        else:
            res.pop()
        res.append("R")
        right  = self.dfs(node.right,target,res)
        if right:
            return right
        else:
            res.pop()
        return None
        
            