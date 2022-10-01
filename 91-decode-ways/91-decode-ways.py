class Solution:
    def numDecodings(self, s: str) -> int:
        codes = set(str(c) for c in range(1,27))
        # print(codes)
        @lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return 1
            
            res = 0
            if i < len(s)-1 and s[i:i+2] in codes:
                res += dfs(i+2)
            
            if s[i] in codes:
                res += dfs(i+1)
            return res
        
        return dfs(0)