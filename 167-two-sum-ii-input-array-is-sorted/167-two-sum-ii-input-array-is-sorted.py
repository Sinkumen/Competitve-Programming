class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            cur = nums[left]+nums[right]
            if cur == target:
                return [left+1,right+1]
            if cur > target:
                right -= 1
            else:
                left += 1
        return []