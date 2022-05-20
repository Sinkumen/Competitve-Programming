class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        start = None
        empty = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    empty += 1
                if grid[i][j] == 1:
                    start = (i,j)
        ans = 0           
        def dfs(x,y,visited,walk):
            nonlocal ans
            if grid[x][y] == 2 and walk == empty:
                ans += 1
                return
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx,ny) not in visited and grid[nx][ny] != -1:
                        visited.add((nx,ny))
                        dfs(nx,ny,visited,walk+1)
                        visited.remove((nx,ny))

        dfs(start[0],start[1],set([start]),0)
        return ans
                    
                    
                