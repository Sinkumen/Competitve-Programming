class Solution:
    def knightDialer(self, n: int) -> int:
        G = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        M = 10**9 + 7
        @cache
        def dfs(v, i):
            if i == 1: return 1
            res = 0
            for w in G[v]:
                res = (res + dfs(w, i-1)) % M
            return res
        return sum(dfs(v,n) for v in range(10)) % M