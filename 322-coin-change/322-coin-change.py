class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(cur):
            if cur == amount:
                return 0
            if cur > amount:
                return -1
            ans = float("inf") 
            for i in range(len(coins)):
                res = dfs(cur+coins[i])
                if res != -1:
                    ans = min(ans,res)
               
            return -1 if ans == float("inf") else ans + 1
                
           
        
        return dfs(0)
                
            
            
            
            