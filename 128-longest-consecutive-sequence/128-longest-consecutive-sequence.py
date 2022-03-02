class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev = set(nums)
        ans = defaultdict(int)
        m = min(nums)
        
        for num in nums:
            curr = 1
            for i in range(num - 1, m - 1, -1):
                if i in ans:
                    curr += ans[i]
                    break
                elif i in prev:
                    curr += 1
                else:
                    break
            ans[num] = curr
        return max(ans.values())