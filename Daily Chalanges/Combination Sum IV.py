class Solution:
    def __init__(self):
        self.count = 0

    def combinationSum4(self, nums, target: int) -> int:
        numset = set(nums)
        memory = {}

        def helper(curSum):
            nonlocal memory
            if curSum in memory:
                self.count += memory[curSum]
                return memory[curSum]
            if curSum == target:
                self.count += 1
                return 1
            if curSum > target:
                return 0
            diff = target - curSum
            res = 0
            for i in range(1, diff+1):
                if i in numset:
                    res += helper(curSum+i)
            memory[curSum] = res
            return res
        for num in nums:
            helper(num)

        return self.count
