class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
  
        diff = float("inf")
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if abs(sum-target) < abs(diff):
                    diff = target-sum
                if sum > target:
                    right -= 1
                else:
                    left += 1
            if diff == 0: break 
        return target - diff
            