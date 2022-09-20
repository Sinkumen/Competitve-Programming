class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def find(nums1,nums2):
            ans = 0
            for offset in range(len(nums1)):
                count = 0
                for i in range(len(nums2)):
                    if i+offset >= len(nums1): break
                    if nums2[i] == nums1[i+offset]:
                        count += 1
                        ans = max(count,ans)
                    else:
                        count = 0
            return ans
                        
        return max(find(nums1,nums2), find(nums2,nums1))