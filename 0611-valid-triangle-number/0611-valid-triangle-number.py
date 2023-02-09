class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            cur = nums[i]
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > cur:
                    ans += (right - left)
                    right -= 1
                else:
                    left += 1
        return ans
                        