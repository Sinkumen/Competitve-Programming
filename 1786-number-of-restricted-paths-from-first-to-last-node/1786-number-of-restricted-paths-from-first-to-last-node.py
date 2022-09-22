class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        graph = defaultdict(list)
        for fr,to,weight in edges:
            graph[fr].append((to,weight))
            graph[to].append((fr,weight))
            
        dtl = defaultdict(lambda: float("inf"))
        prevState = defaultdict(lambda:float("inf"))
        prevState[n] = 0
        def findShortest():
            queue = [(0,n)]
            while queue:
                level,cur = heapq.heappop(queue)
                dtl[cur] = min(dtl[cur], level)
                for nxt,w in graph[cur]:
                    if prevState[nxt] > (level+w):
                        prevState[nxt] = (level+w)
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
                        
                    
                
                
        