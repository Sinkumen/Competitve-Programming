class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands = []
        def dfs(x,y,connected):
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            connected.add((x,y))
            grid2[x][y] = 0
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < len(grid2) and 0 <= ny < len(grid2[0]):
                    if grid2[nx][ny] == 1:
                        dfs(nx,ny,connected)
            return connected
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    islands.append(dfs(i,j,set()))
        ans = 0
        for island in islands:
            found = True
            for x,y in island:
                if grid1[x][y] == 0:
                    found = False
                    break
            if found: ans += 1
        return ans