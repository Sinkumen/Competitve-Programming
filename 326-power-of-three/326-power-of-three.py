class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return (math.log10(n)/math.log10(3))%1==0 if n > 0 else False