from functools import cache
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        poss = { 0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        dp = [[0 for i in range(10)]for _ in range(n)]
        for i in range(10):
            dp[n-1][i] = 1

        for j in range(n-2,-1,-1):
            for k in range(9,-1,-1):
                summ = 0
                for h in poss[k]:
                    summ = (summ + dp[j+1][h]) % mod
                dp[j][k] = summ
        # print(dp[n-2])
        # print(dp[n-1])
        return sum(dp[0]) % mod
        
                