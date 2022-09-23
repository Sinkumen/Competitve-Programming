class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        graph = defaultdict(list)
        for frm,to in connections:
            graph[frm].append(to)
            graph[to].append(frm)
            
        visited = set()
        def dfs(i):
            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
        ans = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                ans += 1
        return ans-1
                
                