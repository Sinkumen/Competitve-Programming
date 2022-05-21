class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(0,0)])
        visited = set([0])
        while queue:
            cur, level = queue.popleft()
            if cur == amount:
                return level
            for i in range(len(coins)):
                nxt = coins[i] + cur
                if nxt <= amount and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt,level+1))
        return -1
    
#         @lru_cache(None)
#         def dfs(cur):
#             if cur == amount:
#                 return 0
#             if cur > amount:
#                 return -1
#             ans = float("inf") 
#             for i in range(len(coins)):
#                 res = dfs(cur+coins[i])
#                 if res != -1:
#                     ans = min(ans,res)
               
#             return -1 if ans == float("inf") else ans + 1
        
#         return dfs(0)

    
                
            
            
            
            