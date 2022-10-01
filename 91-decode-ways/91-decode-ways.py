class Solution:
    def numDecodings(self, s: str) -> int:
        codes = set(str(c) for c in range(1,27))
        def check(c):
            if c[0] == "0" or not (1 <= int(c) <= 26 ): return False
            return True
        
        # print(check("26"))
        @lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return 1
            
            res = 0
            if i < len(s)-1 and  check(s[i:i+2]):
                res += dfs(i+2)
            
            if check(s[i]):
                res += dfs(i+1)
            return res
        
        return dfs(0)