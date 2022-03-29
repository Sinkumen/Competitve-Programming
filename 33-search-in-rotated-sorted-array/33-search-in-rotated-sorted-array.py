class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[start]:
                if nums[mid] < target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] > nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                start += 1
        return -1
            
       
            
        