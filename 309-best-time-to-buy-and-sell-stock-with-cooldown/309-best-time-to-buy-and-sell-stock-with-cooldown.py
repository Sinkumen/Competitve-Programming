class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache()
        def dp(idx,buy):
            if idx >= len(prices):
                return 0
            
            if buy:
                profit = 0
                profit = max(profit,dp(idx+1,False)-prices[idx])
                profit = max(profit,dp(idx+1,True))
                return profit
            else:
                profit = 0
                profit = max(profit,dp(idx+2,True)+prices[idx])
                profit = max(profit,dp(idx+1,False))
                return profit

        return dp(0,True)
                    
                    
                
                
        