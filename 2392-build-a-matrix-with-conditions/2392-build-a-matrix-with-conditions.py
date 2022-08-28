class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rindegree = [0]*(k+1)
        cindegree = [0]*(k+1)
        rgraph = defaultdict(list)
        cgraph = defaultdict(list)
        cvisited = set()
        rvisited = set()
        for rc in rowConditions:
            rc = tuple(rc)
            if rc not in cvisited:
                cvisited.add(rc)
                rgraph[rc[0]].append(rc[1])
                rindegree[rc[1]] += 1
        for cc in colConditions:
            cc = tuple(cc)
            if cc not in rvisited:
                rvisited.add(cc)
                cgraph[cc[0]].append(cc[1])
                cindegree[cc[1]] += 1
        # print(rgraph)
        # print(cindegree)
        def find(indegree,graph):
            queue = deque()
            for i in range(1,k+1):
                if not indegree[i]:
                    queue.append(i)
            # print("q",queue)
            rows = []
            while queue:
                top = queue.popleft()
                rows.append(top)
                for nxt in graph[top]:
                    indegree[nxt] -= 1
                    if not indegree[nxt]:
                        queue.append(nxt)
            if len(rows) == k:
                return rows
            return []
        # print(rindegree)
        row = find(rindegree,rgraph)
        col = find(cindegree,cgraph)
        ans = [[0 for _ in range(k)] for _ in range(k)]
        # print(row,col,rgraph)
        if row and col:
            pos = defaultdict(list)
            for i in range(len(row)):
                pos[row[i]].append(i)
            for i in range(len(col)):
                pos[col[i]].append(i)
            # print(pos)
            # print(ans)
            for i in range(1,k+1):
                ans[pos[i][0]][pos[i][1]] = i
            
            return ans
        return []
    """
[0,0,1],
[0,3,0],
[2,0,0]]
    """
            
        