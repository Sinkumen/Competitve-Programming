# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = deque([root])
       
        while queue:
            mod = level % 2
            prev = 0 if not mod else float("inf")
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if (mod and cur.val >= prev) or (not mod and cur.val <= prev) or cur.val%2 == mod:
                    return False
                prev = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return True
                
        