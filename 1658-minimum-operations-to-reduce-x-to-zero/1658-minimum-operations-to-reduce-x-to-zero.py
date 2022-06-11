class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            pre.append(s)
        suf = [0]*len(nums)
        s = 0
        for i in range(len(nums)-1,-1,-1):
            s += nums[i]
            suf[i] = s
            
        def search(n,arr,pre):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] == n:
                    return mid
                elif arr[mid] > n:
                    if pre:
                        right = mid -1 
                    else:
                        left = mid + 1
                else:
                    if pre:
                        left = mid + 1     
                    else:
                        right = mid - 1 
            return -1

        def binary(arr1,arr2,pre):
            ans = float("inf")
            for i in range(len(nums)):
                if arr1[i] == x:
                    ans = min(ans,i+1) if pre else min(ans,len(nums)-i)
                    continue
                if arr1[i] > x:
                    continue
                if (pre and arr1[-1] > x) or (not pre and arr1[0] > x):
                    res = search(x - arr1[i],arr2,not pre)
                    if res != -1:
                        step = (i + 1 + (len(nums)-res)) if pre else (res + 1 + (len(nums)-i))
                        ans = min(step,ans)
            return ans
        
        temp = min(binary(pre,suf,True),binary(suf,pre,False))
        return temp if temp < float("inf") else -1
                        
