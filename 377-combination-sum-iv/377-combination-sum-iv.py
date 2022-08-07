class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(total):
            if total == target:
                return 1
            res = 0
            for nxt in nums:
                if total + nxt <= target:
                    res += dfs(total + nxt)
            return res
        return dfs(0)
                