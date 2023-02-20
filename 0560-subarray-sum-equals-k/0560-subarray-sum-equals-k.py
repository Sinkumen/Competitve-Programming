class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = defaultdict(int)
        prev[0] += 1  
        ans = 0
        p = 0
        for i in range(len(nums)):
            num = nums[i]
            p += num
            diff = p-k
            if diff in prev:
                ans += prev[diff]
            prev[p] += 1
        return ans