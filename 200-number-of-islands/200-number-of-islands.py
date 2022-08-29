class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            nonlocal visited
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for direc in directions:
                nx = i + direc[0]
                ny = j + direc[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if (nx,ny) not in visited and grid[nx][ny] == "1":
                        visited.add((nx,ny))
                        dfs(nx,ny)
        visited = set()
        ans = 0       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    dfs(i,j)
                    ans += 1
       
        return ans
                    