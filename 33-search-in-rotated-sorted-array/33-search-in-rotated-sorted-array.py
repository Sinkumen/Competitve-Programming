class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = (start + end)//2
                if nums[mid] >= nums[0]:
                    start = mid + 1
                else:
                    end = mid - 1
            return start
        
        pivot = findPivot()
        start = 0 if target >= nums[0] else pivot
        end = pivot - 1  if target >= nums[0] else len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
            
       
            
        