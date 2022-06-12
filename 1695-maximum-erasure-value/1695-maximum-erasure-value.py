class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left,right = 0,0
        found = set()
        ans = 0
        sum_ = 0
        while right < len(nums):
            r = nums[right]
            while r in found:
                l = nums[left]
                sum_ -= l
                found.remove(l)
                left += 1
            sum_ += r
            ans = max(ans,sum_)
            found.add(r)
            right += 1
        return ans
            