# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root.left and not root.right:
                return (root.val,0)
            left = None
            right = None

            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            if left and right:
                if left[1] == right[1]:
                    return (left[0] + right[0], left[1] + 1)
                elif left[1] > right[1]:
                    return (left[0],left[1]+1)
                else:
                    return (right[0],right[1]+1)
            elif left:
                return (left[0],left[1]+1)
            else:
                return (right[0],right[1]+1)
        return dfs(root)[0]
        
        