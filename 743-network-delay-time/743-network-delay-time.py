class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for edge in times:
            source,target,time = edge
            adjList[source].append((target,time))
        heap = [(0,k)]
        visited = set()
        while heap:
            time,node = heapq.heappop(heap)
            visited.add(node)
            if len(visited) == n:
                return time
            for nxt in adjList[node]:
                if nxt[0] not in visited:
                    heapq.heappush(heap,(nxt[1]+time,nxt[0]))
        return -1
            