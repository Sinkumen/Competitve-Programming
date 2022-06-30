class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2 == 0:
            center1 = 0
            center2 = 0
            for x in nums:
                center1 += abs(nums[(len(nums)//2)-1]-x)
                center2 += abs(nums[(len(nums)//2)]-x)
            return min(center1,center2)
        else:
            ans = 0
            for x in nums:
                ans += abs(nums[len(nums)//2]-x)
            return ans