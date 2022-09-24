# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def dfs(node,total,res):
            if not node.left and not node.right:
                if total+node.val == targetSum:
                    res.append(node.val)
                    ans.append([n for n in res])
                    res.pop()
                return
            res.append(node.val)
            if node.left: dfs(node.left,total+node.val,res)
            if node.right: dfs(node.right,total+node.val,res)
            res.pop()
            
        dfs(root,0,[])
        return ans
            