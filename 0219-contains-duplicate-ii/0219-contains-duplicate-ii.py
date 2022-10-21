class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = []
        for i in range(len(nums)):
            idx.append((nums[i],i))
        idx.sort()
        # print(idx)
        for i in range(1,len(idx)):
            if idx[i][0] ==  idx[i-1][0] and abs(idx[i][1] - idx[i-1][1]) <= k:
                return True
        return False