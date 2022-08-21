# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if not node:
                return (0,0,False)
            if node.val == start:
                return (0,0,True)
           

            left = dfs(node.left)
            right = dfs(node.right)
            # print(node.val,left,right)
            if left[2] or right[2]:
                temp = (left[0] + right[0] + 1)
                gl = max(left[1],right[1],temp)
                if left[2]: return (left[0] + 1,gl,True)
                if right[2]: return (right[0] + 1,gl,True)
            else:
                gl = max(left[0]+1,right[0]+1)
                return (gl,gl,False)
        def dfs2(node):
            if not node:
                return (0,False)
            left = dfs2(node.left)
            right = dfs2(node.right)
            
            if node.val == start:
                return (max(left[0],right[0]),True)
            if left[1]:
                return left
            if right[1]:
                return right
            return (max(left[0],right[0])+1,False)
        before = dfs(root)
        after = dfs2(root)
        # print(before,after)
        return max(before[1],after[0])