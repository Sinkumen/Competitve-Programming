class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        multi = {}
        for n in arr:
            left =  0
            right = len(arr)-1
            res = set()
            while left <= right:
                m = arr[left]*arr[right]
                if m == n:
                    res.add((arr[left],arr[right]))
                    res.add((arr[right],arr[left]))
                    left += 1
                    right -= 1
                elif m < n:
                    left += 1
                else:
                    right -= 1
            if res:
                multi[n] = res

        mod = 10**9 + 7
        @lru_cache(None)
        def dfs(num):
            if num in multi:
                sub = 0
                for nxt in multi[num]:
                    first = dfs(nxt[0])
                    second = dfs(nxt[1])
                    if first:
                        sub += first
                    if second:
                        sub += second 
                    if first and second:
                        sub += (first*second)
                    sub += 1
        
                return sub
            return 0
        
        ans = len(arr)
        for key in multi.keys():
            ans += dfs(key)
        return ans%mod
        