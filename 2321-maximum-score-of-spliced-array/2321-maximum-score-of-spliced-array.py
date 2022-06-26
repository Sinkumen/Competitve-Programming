class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        def findSub(arr1,s1,arr2,res):
            left = 0
            right = 0
            cur = 0
            while right < len(arr1):
                diff = arr2[right] - arr1[right]
                cur += diff
                while cur < 0:
                    diff = arr2[left] - arr1[left]
                    cur -= diff
                    left += 1
                res = max(res,s1+cur)
                right += 1
            return res
        return max(findSub(nums1,sum1,nums2,max(sum1,sum2)),findSub(nums2,sum2,nums1,max(sum1,sum2)))
                
            
        
        