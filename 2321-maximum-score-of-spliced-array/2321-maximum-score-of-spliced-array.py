class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        def findSub(arr1,s1,arr2,res):
            right = 0
            benefit = 0
            while right < len(arr1):          
                diff = arr2[right] - arr1[right]
                benefit += diff
                if benefit < 0:
                    benefit = 0
                res = max(res,s1+benefit)
                right += 1
            return res 
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        one_to_two = findSub(nums1,sum1,nums2,max(sum1,sum2))
        two_to_one = findSub(nums2,sum2,nums1,max(sum1,sum2))
        
        return max(one_to_two,two_to_one)