class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        direcs = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(x,y):
            res = 1
            for direc in direcs:
                nx = x + direc[0]
                ny = y + direc[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1 and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        res += dfs(nx,ny)
            return res

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    temp = dfs(i,j)
                    ans = max(ans,temp)
        return ans
            