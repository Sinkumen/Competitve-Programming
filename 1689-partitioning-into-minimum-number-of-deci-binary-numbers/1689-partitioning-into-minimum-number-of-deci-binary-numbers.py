class Solution:
    def minPartitions(self, n: str) -> int:
        nums = [int(x) for x in n]
        return max(nums)
        