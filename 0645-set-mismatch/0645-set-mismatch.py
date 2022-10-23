class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        v = set()
        ans = [0,0]
        for n in range(1,len(nums)+1):
            if n not in s:ans[1] = n
            if nums[n-1] in v: ans[0] = nums[n-1]
            v.add(nums[n-1])

        return ans