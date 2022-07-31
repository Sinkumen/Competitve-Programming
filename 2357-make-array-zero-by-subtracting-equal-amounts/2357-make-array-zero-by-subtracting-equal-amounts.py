class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in set(nums): 
            if x: ans += 1
        return ans