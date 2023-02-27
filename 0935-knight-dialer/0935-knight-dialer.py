from functools import cache
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        poss = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        ans = 0
        @cache
        def dfs(i,size):
            if size == n:
                return 1
            res = 0
            for nxt in poss[i]:
                res += dfs(nxt,size+1) % mod
            return res % mod
                
        for i in range(10):
            ans += dfs(i,1)
        return ans % mod
                