class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dp(idx,buy,mem):
            if (idx,buy) in mem:
                return mem[(idx,buy)]
            if idx >= len(prices):
                return 0
            if buy:
                profit = 0
                for i in range(idx+1,len(prices)):
                    cur = prices[idx]
                    nxt = prices[i]
                    diff = prices[i] - prices[idx]
                    if nxt > cur:
                        profit = max(profit,diff + dp(i,False,mem))
                mem[(idx,buy)] = profit
                return profit
            else:
                profit = 0
                for i in range(idx+2,len(prices)):
                    profit = max(profit, dp(i,True,mem))
                mem[(idx,buy)] = profit
                return profit
        ans = 0
        mem = {}
        for i in range(len(prices)):
            ans = max(ans,dp(i,True,mem))
        return ans
                    
                    
                
                
        