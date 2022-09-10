class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,bought,rem):
            if i >= len(prices) or not rem:
                return 0
            res = 0
            if bought:
                w = prices[i] + dfs(i+1,False,rem-1)
                wo = dfs(i+1,True,rem)
                return max(w,wo)
            else:
                w = dfs(i+1,True,rem) - prices[i]
                wo = dfs(i+1,False,rem)
                # print(i,w,wo)
                return max(w,wo)
                
        return dfs(0,False,k)