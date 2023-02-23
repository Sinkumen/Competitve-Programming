class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        mem = {1:1}
        def getPower(n):
            if n in mem:
                return mem[n]
            if n%2 == 0:
                mem[n] = 1 + getPower(n // 2)
            else:
                mem[n] = 1 + getPower(n * 3 + 1)
            return mem[n]
        return sorted(range(lo,hi+1),key=lambda x: getPower(x))[k-1]