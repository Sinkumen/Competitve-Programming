class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        graph = defaultdict(list)
        for fr,to,weight in edges:
            graph[fr].append((to,weight))
            graph[to].append((fr,weight))
            
        dtl = {n:0}
        def findShortest():
            queue = [(0,n)]
            visited = set()
            while queue:
                level,cur = heapq.heappop(queue)
                if cur not in visited:
                    dtl[cur] = level
                    visited.add(cur)
                    for nxt,w in graph[cur]:
                        if nxt not in visited:
                            heapq.heappush(queue,(level + w,nxt))
        findShortest()
        # print(dtl)   
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 1
            res = 0
            for nxt,w in graph[i]:
                if dtl[i] > dtl[nxt]:
                    res += dfs(nxt)
            return res
        # print(dtl)
        return dfs(1) % mod
                        