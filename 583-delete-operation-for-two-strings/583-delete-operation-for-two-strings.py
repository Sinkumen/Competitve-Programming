class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dfs(p1,p2):
            if p1 > len(word1)-1 and p2 > len(word2)-1:
                return 0
            if p1 < len(word1) and p2 < len(word2) and word1[p1] == word2[p2]:
                return dfs(p1+1,p2+1)
            
            ans = float("inf")
            if p1 < len(word1):
                ans = min(ans,dfs(p1+1,p2))
            if p2 < len(word2):
                ans = min(ans,dfs(p1,p2+1))
            return ans + 1
        
        return dfs(0,0)
            
            