class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        res=[-1]*len(nums1)
        nums1Idx={num:i for i, num in enumerate(nums1)}
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            #is our current number the next greater element for
            #any num in the stack?
            #if so keep popping off from the stack.
			# and keep updating our result array. 
            while stack and curr>stack[-1]:
                val=stack.pop()
                idx=nums1Idx[val]
                res[idx]=curr
            if curr in nums1Idx:
                stack.append(curr)
        return res