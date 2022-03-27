# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start = self.findPath(root,startValue,[])
        dest = self.findPath(root,destValue,[])
        s = 0
        e = 0
        ans = []
        while s<len(start) and e<len(dest) and start[s] == dest[e]:
            s += 1
            e += 1
        ans.append("U"*(len(start)-s))
        ans.extend(dest[e:])
        
        return "".join(ans)
            
    def findPath(self,node,target,path):
        if node.val == target:
            return path
        if node.left:
            path.append("L")
            res = self.findPath(node.left,target,path)
            if res:
                return res
            path.pop()
        if node.right:
            path.append("R")
            res = self.findPath(node.right,target,path)
            if res:
                return res
            path.pop()
        
            