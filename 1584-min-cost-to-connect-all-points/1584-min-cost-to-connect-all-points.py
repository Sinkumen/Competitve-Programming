class Solution:

    def minCostConnectPoints(self, points):
        f = {}
        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(x)] = find(y)
        edges = []
        for i, [x1, y1] in enumerate(points):
            for [x2, y2] in points[i+1:]:
                if x1 != x2 or y1 != y2:
                    heapq.heappush(edges, (abs(y1-y2)+abs(x1-x2), x1, y1, x2, y2))
        ans = 0 
        while edges:
            weight, x1, y1, x2, y2 = heapq.heappop(edges)
            if find((x1, y1)) != find((x2, y2)):
                union((x1, y1), (x2, y2))
                ans += weight
        return ans
        
        

        