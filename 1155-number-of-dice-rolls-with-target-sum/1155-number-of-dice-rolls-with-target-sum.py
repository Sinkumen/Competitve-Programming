class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def dfs(i,total):
            if i >= n:
                if total == target: return 1
                return 0
            res = 0
            for j in range(1,k+1):
                if j+total <= target:
                    res += dfs(i+1,total + j)
            return res % mod
        return dfs(0,0) % mod