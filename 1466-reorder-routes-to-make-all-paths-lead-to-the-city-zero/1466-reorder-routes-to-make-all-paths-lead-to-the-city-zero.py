class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph  = defaultdict(list)
        incoming = defaultdict(list)
        for frm,to in connections:
            graph[frm].append(to)
            incoming[to].append(frm)
        
        def dfs(node,visited):
            ans = 0
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    ans += dfs(nxt,visited) + 1
            for prev in incoming[node]:
                if prev not in visited:
                    visited.add(prev)
                    ans += dfs(prev,visited)          
            return ans
        return dfs(0,set([0]))
                
        