class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = []
        cur = 1
        ans = float("-inf")
        for i in range(len(nums)):
            if not nums[i]:
                pre.append(0)
                ans = max(ans,0)
                cur = 1
            else:
                cur *= nums[i]
                ans = max(ans,cur)
                pre.append(cur)
            
        suf = [1]*len(nums)
        cur = 1
        for i in range(len(nums)-1,-1,-1):
            if not nums[i]:
                suf[i] = 0
                ans = max(ans,0)
                cur = 1
            else:
                cur *= nums[i]
                ans = max(ans,cur)
                suf[i] = cur
        return ans