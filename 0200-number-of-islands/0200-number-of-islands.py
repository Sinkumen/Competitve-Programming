class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(i,j):
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for d in dirs:
                ni = d[0] + i
                nj = d[1] + j
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if (ni,nj) not in visited and grid[ni][nj] == "1":
                        visited.add((ni,nj))
                        dfs(ni,nj)
                        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        return ans
                        
            