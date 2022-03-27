class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            maxx = 0
            for j in range(i,len(nums)):
                if nums[j] > nums[i]:
                    maxx = max(dp[j],maxx)
            dp[i] = maxx + 1
        return max(dp)
            
            