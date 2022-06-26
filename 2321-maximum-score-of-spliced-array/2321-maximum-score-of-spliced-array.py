class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def findSub(arr1,s1,arr2,res):
            left = 0
            right = 0
            benefit = 0
            while right < len(arr1):
                # calulate the benefit we can get if we swap the element in the right pointer
                diff = arr2[right] - arr1[right]
                benefit += diff
        
                # if the benefit is negative that means we need to undo the swaps we have made so far
                # by moving the left pointer 
                # start over from the position of the pointers
                while benefit < 0:
                    diff = arr2[left] - arr1[left]
                    benefit -= diff
                    left += 1
                res = max(res,s1+benefit)
                right += 1
            return res
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        # Try to maximize the first array by swaping subarrays from the second array
        one_to_two = findSub(nums1,sum1,nums2,max(sum1,sum2))
		
		 # Try to maximize the second array by swaping subarrays from the first array
        two_to_one = findSub(nums2,sum2,nums1,max(sum1,sum2))
        
        return max(one_to_two,two_to_one)