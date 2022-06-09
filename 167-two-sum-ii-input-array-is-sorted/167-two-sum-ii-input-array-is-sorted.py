class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(n,i) for i,n in enumerate(nums)]
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            cur = nums[left][0]+nums[right][0]
            if cur == target:
                return [nums[left][1]+1,nums[right][1]+1]
            if cur > target:
                right -= 1
            else:
                left += 1
        return []