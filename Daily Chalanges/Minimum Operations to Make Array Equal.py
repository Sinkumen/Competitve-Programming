class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        first = 1
        last = (n-1)*2 + 1
        req = (first + last)//2
        for i in range(ceil(n/2)):
            operations += (req - (i*2 + 1))
        return operations
