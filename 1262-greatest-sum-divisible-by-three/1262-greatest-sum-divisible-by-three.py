class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        one1,one2 = float("inf"),float("inf")
        two1,two2 = float("inf"), float("inf")
        total = 0
        
        for num in nums:
            total += num
            if num%3 == 1:
                if num < one1:
                    one2 = min(one2,one1)
                    one1 = num
                else:
                    one2 = min(one2,num)
            elif num % 3 == 2:
                if num < two1:
                    two2 = min(two2,two1)
                    two1 = num
                else:
                    two2 = min(two2,num)
        if total%3 == 0:
            return total
        
        if total%3 == 1:
            return total - min(two1+two2,one1)
        
        return total - min(one1+one2,two1)