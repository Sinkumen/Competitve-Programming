from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        ans = [0]*len(nums)
        for i in range(len(nums)):
            arr.append((nums[i],i))
        
        def merge(arr):
            if len(arr)==1:
                return arr
            mid = len(arr)//2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            
            l = 0
            r = 0
            res = []
            smaller = 0
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    res.append(right[r])
                    smaller += 1
                    r += 1
                else:
                    ans[left[l][1]] += smaller
                    res.append(left[l])
                    l += 1
                    
            while l < len(left):
                ans[left[l][1]] += smaller
                res.append(left[l])
                l += 1
                
            while r < len(right):
                res.append(right[r])
                r += 1
            return res
        temp = merge(arr)

        return ans
            
        
            
                    
            
        
        