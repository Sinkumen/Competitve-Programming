class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bins = []
        for i in range(1,n+1):
            bins.append(bin(i)[2:])
        return int("".join(bins),2) % (10**9 + 7)