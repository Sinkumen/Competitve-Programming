class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre = [0]
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            pre.append(s)
        suf = [0]*len(nums)
        s = 0
        for i in range(len(nums)-1,-1,-1):
            s += nums[i]
            suf[i] = s
        suf.append(0)
            
        def search(n,arr):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] == n:
                    return mid
                elif arr[mid] > n:
                    left = mid + 1
                else:
                    right = mid - 1 
            return -1

        ans = float("inf")
        for i in range(len(nums)):
            if pre[i] == x:
                ans = min(ans,i) 
                continue
            if pre[i] > x:
                continue

            if pre[-1] >= x:
                res = search(x - pre[i],suf)
                if res != -1:
                    step = (i + (len(nums)-res)) if pre else (res + (len(nums)-i))
                    ans = min(step,ans)
        return ans if ans < float("inf") else -1
      
                        
