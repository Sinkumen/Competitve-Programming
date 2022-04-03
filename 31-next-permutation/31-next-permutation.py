class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                cur = i+1
                while cur < len(nums):
                    if nums[i] >= nums[cur]:
                        found = True
                        nums[i],nums[cur-1] = nums[cur-1],nums[i]
                        break
                    cur += 1
                if not found:
                    nums[i],nums[cur-1] = nums[cur-1],nums[i]
                left = i+1
                right = len(nums)-1
                while left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1
                    right -= 1

                return
                
        nums.sort()
        return
        