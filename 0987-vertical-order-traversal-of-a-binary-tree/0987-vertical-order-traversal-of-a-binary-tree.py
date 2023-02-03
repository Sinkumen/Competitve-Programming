# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cells = defaultdict(list)
        def dfs(node,row,col):
            nonlocal cells
            cells[(row,col)].append(node.val)
            if node.left:
                dfs(node.left,row+1,col-1)
            if node.right:
                dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        ans = []
        cols = defaultdict(list)
        for r,c in sorted(cells.keys()):
            cols[c].extend(sorted(cells[(r,c)]))
        for c in sorted(cols.keys()):
            ans.append(cols[c])
        return ans