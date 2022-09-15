class Solution:
    def isUgly(self, n: int) -> bool:
        req = set([1,2,3,5])
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if i not in req:
                    return False
                factors.append(i)
        if n not in req:
            return False
        return True