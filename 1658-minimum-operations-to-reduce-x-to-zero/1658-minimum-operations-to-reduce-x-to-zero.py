class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        window = sum(nums) - x
        if window < 0:
            return - 1
        left,right = 0,0
        ans = -1
        cur = 0
        while right < len(nums):
            cur += nums[right]
            while cur > window:
                cur -= nums[left]
                left += 1
            if cur == window:
                ans= max(ans,right-left+1)
            right += 1
            
        return len(nums) - ans if ans >= 0 else -1
        
      
                        
