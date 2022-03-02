# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        maxx = (nums[0],0)
        for i in range(len(nums)):
            if nums[i] > maxx[0]:
                maxx = (nums[i],i)

        root = TreeNode(maxx[0])
        root.left = self.constructMaximumBinaryTree(nums[:maxx[1]])
        root.right = self.constructMaximumBinaryTree(nums[maxx[1]+1:])

        return root
