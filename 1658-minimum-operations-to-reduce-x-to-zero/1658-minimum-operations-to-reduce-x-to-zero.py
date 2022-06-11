class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def search(n):
            left = 0
            right = len(pre)-1
            while left <= right:
                mid = (left + right)//2
                if pre[mid] == n:
                    return mid
                elif pre[mid] > n:
                    right = mid - 1 
                else:
                    left = mid + 1        
            return -1
        
        pre = [0]
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            pre.append(s)
        if pre[-1] < x:
            return -1
        
        ans = float("inf")
        nums.append(0)
        s = 0
        for i in range(len(nums)-1,-1,-1):
            s += nums[i]
            res = search(x - s)
            if res != -1:
                step = res + (len(nums)-i-1)
                ans = min(step,ans)
            

        return ans if ans < float("inf") else -1
      
                        
