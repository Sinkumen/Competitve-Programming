class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x,y,visited,mem):
            if (x,y) in mem:
                return mem[(x,y)]
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            maxx = 0
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if matrix[nx][ny] > matrix[x][y] and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        maxx = max(maxx,dfs(nx,ny,visited,mem))
                        visited.remove((nx,ny))
            mem[(x,y)] = maxx + 1
            return mem[(x,y)]
        
        n = len(matrix)
        m = len(matrix[0])
        ans = 1  
        mem = {}
        for i in range(n):
            for j in range(m):
                ans = max(ans,dfs(i,j,set(),mem))
        return ans
        