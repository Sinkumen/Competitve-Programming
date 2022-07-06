class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        f0 = 0
        f1 = 1
        for i in range(2,n+1):
            temp = f1
            f1 = f0 + f1
            f0 = temp
        return f1