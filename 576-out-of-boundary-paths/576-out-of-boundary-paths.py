class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = (10**9)+7
        direcs = [(0,1),(1,0),(-1,0),(0,-1)]
        @lru_cache(None)
        def dfs(x,y,move):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if not move:
                return 0
            res = 0
            for direc in direcs:
                nx = x+direc[0]
                ny = y+direc[1]
                res += dfs(nx,ny,move-1)
            return res      
        return dfs(startRow,startColumn,maxMove)%mod
        
                
            