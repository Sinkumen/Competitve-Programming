class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        _min = min(nums)
        _max = max(nums)
        arr = [0]*(_max+1)
        for n in nums:
            arr[n] += n
        dp = [0]*(_max+1)
        dp[_min] = arr[_min]
        for i in range(2,len(arr)):
            dp[i] = max(dp[i-1],dp[i-2] + arr[i])

        return dp[-1]
            