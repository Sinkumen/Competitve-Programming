class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(n):
            ans = 0
            while n != 1:
                if n%2 == 0:
                    n = n // 2
                else:
                    n = n * 3 + 1
                ans += 1
            return ans
        return sorted(range(lo,hi+1),key=lambda x: getPower(x))[k-1]