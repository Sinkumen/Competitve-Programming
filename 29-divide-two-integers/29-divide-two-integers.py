class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        a = abs(dividend)
        b = abs(divisor)
        
        ans = 0
        
        while a >= b:
            mul = 1
            temp = b
            while a >= temp:
                a -= temp
                ans += mul
                mul += mul
                temp += temp
            
        if (divisor > 0 > dividend) or (divisor < 0 < dividend):
            return -ans
        
        return min(2147483647,max(-2147483648,ans))
            