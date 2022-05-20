class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        @lru_cache(None)
        def dfs(x,y):
            if x == n-1 and y == m-1:
                return 1
            dirs = [(0,1),(1,0)]
            ans = 0
            for d in dirs:
                nx = x+d[0]
                ny = y+d[1]
                if 0 <= nx < n and 0 <= ny < m and obstacleGrid[nx][ny] == 0:
                    ans += dfs(nx,ny)
            return ans
                    
        if obstacleGrid[0][0] == 0:
            return dfs(0,0)
        return 0
                    