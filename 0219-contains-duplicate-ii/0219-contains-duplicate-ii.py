class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}
        
        for i in range(len(nums)):
            if nums[i] in idx and abs(idx[nums[i]]-i) <= k:
                return True
            else:
                idx[nums[i]] = i
        return False
                
        