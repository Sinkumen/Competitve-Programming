class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(x,y):
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            maxx = 0
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if matrix[nx][ny] > matrix[x][y]:
                        maxx = max(maxx,dfs(nx,ny))       
            return maxx + 1
        
        n = len(matrix)
        m = len(matrix[0])
        ans = 1  
        for i in range(n):
            for j in range(m):
                ans = max(ans,dfs(i,j))
        return ans
        