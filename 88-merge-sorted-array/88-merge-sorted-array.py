class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(1,len(nums2)+1):
            nums1[-i] = nums2[i-1]
            
        nums1.sort()    
            
        