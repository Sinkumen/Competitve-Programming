class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            grid[i][j] = 0
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for direc in directions:
                nx = i + direc[0]
                ny = j + direc[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == "1":
                        dfs(nx,ny)
        ans = 0       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
       
        return ans
                    