class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        rel = defaultdict(dict)
        for i in range(len(equations)):
            x,y = equations[i]
            rel[x][y] = values[i]
            rel[y][x] = 1/values[i]
        def find(start,end,visited):
            if end in rel[start]:
                return rel[start][end]

            for nxt in rel[start].keys():
                if nxt not in visited:
                    visited.add(nxt)
                    res = find(nxt,end,visited)
                    if res != -1:
                        return rel[start][nxt] * res
            return -1
        ans = []
        for start,end in queries:
            ans.append(find(start,end,set([start])))
        return ans
            