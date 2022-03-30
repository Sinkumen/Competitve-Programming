# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def dfs(node):
            if not node.left and not node.right:
                dic[0].append(node.val)
                return 0
            left = right = 1
            if node.left:
                left += dfs(node.left)
            if node.right:
                right += dfs(node.right)
            mx = max(left,right)
            dic[mx].append(node.val)
            return mx
        dfs(root)
        ans = []
        for key in dic.keys():
            ans.append(dic[key])
        return ans
            