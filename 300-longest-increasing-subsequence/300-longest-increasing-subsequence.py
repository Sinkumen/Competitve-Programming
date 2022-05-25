class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        srtd = []
        for i in range(len(nums)):
            if not srtd or srtd[-1] < nums[i]:
                srtd.append(nums[i])
            else:
                left = 0
                right = len(srtd)-1
                idx = 0
                while left <= right:
                    mid = (left + right)//2
                   
                    if srtd[mid] >= nums[i]:
                        idx = mid
                        right = mid- 1
                    else:
                        left = mid + 1
                
                srtd[idx] = nums[i]
        return len(srtd)
                
        
            
            