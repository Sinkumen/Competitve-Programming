class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)-1
        odds = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odds.append(i)
        if len(odds) < k:
            return 0
        left = 0
        right = k-1
        ans = 0
        while right < len(odds):
            before = odds[left] if not left else (odds[left] - odds[left-1] - 1)
            after = n - odds[right] if right == len(odds)-1 else (odds[right+1] - odds[right]-1)
            ans += before + after + (after*before) + 1
            left += 1
            right += 1

        return ans