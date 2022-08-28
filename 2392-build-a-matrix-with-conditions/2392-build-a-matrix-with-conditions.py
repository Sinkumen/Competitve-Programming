class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def find(conditions):
            indegree = [0]*(k+1)
            graph = defaultdict(list)
            for c in conditions:
                c = tuple(c)
                visited = set()
                if c not in visited:
                    visited.add(c)
                    graph[c[0]].append(c[1])
                    indegree[c[1]] += 1
            queue = deque()
            for i in range(1,k+1):
                if not indegree[i]:
                    queue.append(i)

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

        row = find(rowConditions)
        col = find(colConditions)
        ans = [[0 for _ in range(k)] for _ in range(k)]

        if row and col:
            pos = defaultdict(list)
            for i in range(len(row)):
                pos[row[i]].append(i)
            for i in range(len(col)):
                pos[col[i]].append(i)

            for i in range(1,k+1):
                ans[pos[i][0]][pos[i][1]] = i
            
            return ans
        return []

            
        