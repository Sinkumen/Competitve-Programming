class Solution:
    def rob(self, nums) -> int:

        memory = {}

        def robMax(i):
            nonlocal memory
            if i in memory:
                return memory[i]
            if i == len(nums)-1 or i == len(nums)-2:
                return nums[i]
            two = robMax(i+2)
            three = robMax(i+3) if i+3 <= len(nums)-1 else 0
            memory[i] = max(two, three) + nums[i]
            return max(two, three) + nums[i]
        maxx = 0
        for i in range(len(nums)):
            maxx = max(robMax(i), maxx)
        return maxx
