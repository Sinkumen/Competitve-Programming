class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prevCount = [0]*(len(nums)+1)
        prevCount[0] = 1
        res = 0
        count = 0
        for num in nums:
            if num % 2 == 1:
                count += 1
            prevCount[count] += 1
            if prevCount[count - k]:
                res += prevCount[count - k]
        return res