class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in num_set:
                cur = num
                count = 0
                while cur in num_set:
                    count += 1
                    cur += 1
                ans = max(ans,count)
        return ans