class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        srtd = sorted(nums)
        start = -1
        end = -1
        for i in range(len(nums)):
            if srtd[i] != nums[i]:
                if start == -1:
                    start = i
                else:
                    end = i+1
        return end - start
        