class Solution:
    def subarraySum(self, nums, k: int) -> int:
        prefix = {0: 1}
        p = 0
        count = 0
        for i in range(len(nums)):
            p += nums[i]
            if p - k in prefix:
                count += prefix[p-k]
            if p not in prefix:
                prefix[p] = 1
            else:
                prefix[p] += 1

        return count
