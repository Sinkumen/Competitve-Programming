# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue = deque([root])
            ans = [] 
            while queue:
                ans.append([node.val for node in queue])
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    if cur.left: queue.append(cur.left)
                    if cur.right: queue.append(cur.right)
            return ans