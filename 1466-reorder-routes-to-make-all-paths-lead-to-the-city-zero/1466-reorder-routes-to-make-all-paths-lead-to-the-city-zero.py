class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph  = defaultdict(list)
        incoming = defaultdict(list)
        for frm,to in connections:
            graph[frm].append(to)
            incoming[to].append(frm)
        ans = 0
        queue = deque([(0,0)])
        visited = set([0])
        while queue:
            cur,direc = queue.popleft()
            if direc:
                ans += 1
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt,-1))
            for prev in incoming[cur]:
                if prev not in visited:
                    visited.add(prev)
                    queue.append((prev,0))
            
        return ans
                
        