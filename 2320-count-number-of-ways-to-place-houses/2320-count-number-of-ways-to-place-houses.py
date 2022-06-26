class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def dfs(i,place):
            if i == n:
                return 1
            
            if place:
                return dfs(i+1,False)
            
            return dfs(i+1,False) + dfs(i+1,True)

        return (dfs(0,False)**2)%mod