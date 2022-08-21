# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        def dfs(node):
            nonlocal graph
            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    dfs(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    dfs(node.right)
        dfs(root)
        queue = deque([(start,0)])
        visited=set([start])
        while queue:
            cur,level = queue.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt,level+1))
                    
        return level
                    