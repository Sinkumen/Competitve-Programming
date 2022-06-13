class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = float("inf")
        @lru_cache(None)
        def dfs(i,j):
            if i == len(triangle)-1:
                return triangle[i][j]      
            res = min(dfs(i+1,j),dfs(i+1,j+1))
            return res + triangle[i][j]
        
        return dfs(0,0)