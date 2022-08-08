class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        srtd = []
        for num in nums:
            
            if not srtd or srtd[-1] < num:
                srtd.append(num)
            else: 
                left = 0
                right = len(srtd)-1
                idx = 0
                while left <= right:
                    
                    mid = (left + right)//2
                    if srtd[mid] >= num:
                        idx = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                srtd[idx] = num
        return len(srtd)
        
            
            