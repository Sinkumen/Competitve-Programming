# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(set)
        cells = defaultdict(list)
        def dfs(node,row,col):
            nonlocal cols
            if not node:
                return 
            cols[col].add((row,col))
            cells[(row,col)].append(node.val)
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        
        ans = []
        dfs(root,0,0)
        # print(cols)
        # print(cells)
        for key in sorted(cols.keys()):
            arr = []
            for val in sorted(cols[key]): 
                arr.extend(sorted(cells[val]))
            ans.append(arr)
        return ans
            
            