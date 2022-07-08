class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i,k,prev):
            if i >= len(houses):
                if not k:
                    return 0
                return float("inf")

            
            if houses[i] != 0:
                if houses[i] == prev:
                    return dfs(i+1,k,prev)
                elif not k:
                    return float("inf")
                else:
                    return dfs(i+1,k-1,houses[i])
                
            if not k:
                return cost[i][prev-1] + dfs(i+1,k,prev)
            
            res = float("inf")
            for j in range(n):
                paintCost = cost[i][j]
                if j+1 == prev:
                    temp = paintCost + dfs(i+1,k,prev)
                    res = min(temp,res)
                else:
                    temp = paintCost + dfs(i+1,k-1,j+1)
                    res = min(temp,res)
            return res
        
        ans = dfs(0,target,-1)
        return ans if ans != float("inf") else -1
                    