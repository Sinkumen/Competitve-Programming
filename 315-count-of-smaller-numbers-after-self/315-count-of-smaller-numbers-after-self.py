class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        
        def merge(arr):
            if len(arr) == 1:
                return arr
            left = merge(arr[:len(arr)//2])
            right = merge(arr[len(arr)//2:])
            
            l = 0
            r = 0
            les = 0
            res = []
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    les += 1
                    res.append(right[r])
                    r += 1
                else:
                    ans[left[l][1]] += les
                    res.append(left[l])
                    l += 1
            while l < len(left):
                ans[left[l][1]] += les
                res.append(left[l])
                l += 1
            res.extend(right[r:])
            
            return res
        merge([(nums[i],i) for i in range(len(nums))])
        return ans
                