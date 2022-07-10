class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
            else:
                dp[i] = min(dp[i-2],dp[i-1])+nums[i]
        return min(dp[-2],dp[-1])
                
                