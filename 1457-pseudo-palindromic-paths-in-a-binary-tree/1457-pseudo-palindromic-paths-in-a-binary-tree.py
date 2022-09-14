# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node,count):
            if not node:
                return 0
            count[node.val] += 1
            if not node.left and not node.right:
                odds = 0
                # print(count)
                for odd in count:
                    if odd%2 == 1: 
                        odds += 1
                count[node.val] -= 1
                if odds <= 1:
                    return 1
                return 0
            
            left = dfs(node.left,count)
            right = dfs(node.right,count)
            count[node.val] -= 1
            return left + right
        count = [0]*10
        return dfs(root,count)