class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        hasZero = False
        for i in range(len(nums)):
            if not nums[i]:
                hasZero = True
            curr += nums[i]
        for i in range(max(nums)+1):
            total += i
        if not hasZero:
            return 0
        for j in range(1,len(nums)):
            if (total - j) == curr:
                return j
        return len(nums)
            