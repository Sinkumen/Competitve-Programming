class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        summ = nums[0]
        maxx = nums[0]
        for i in range(1,len(nums)):
            summ += nums[i]
            if summ < nums[i]:
                summ = nums[i]
            maxx = max(maxx,summ)
        return maxx