class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = ceil(len(nums)/2)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        l = 0
        r = 0
        ans = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ans.append(left[l])
                l += 1
            else:
                ans.append(right[r])
                r += 1
        ans.extend(left[l:])
        ans.extend(right[r:])
        return ans