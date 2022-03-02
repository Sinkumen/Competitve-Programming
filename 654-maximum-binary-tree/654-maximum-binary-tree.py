# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):
            if l >= len(nums) or l > r:
                return
            if l == r:
                return TreeNode(nums[l])
            maxx = (nums[l],l)
            for i in range(l,r+1):
                if nums[i] > maxx[0]:
                    maxx = (nums[i],i)
           
            root = TreeNode(maxx[0])
            root.left = dfs(l,maxx[1]-1)
            root.right = dfs(maxx[1]+1,r)
            return root
        return dfs(0,len(nums)-1)
