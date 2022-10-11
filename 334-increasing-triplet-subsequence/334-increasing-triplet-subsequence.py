class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ans = 0
        res = []
        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
            else:
                
                left = 0
                right = len(res)-1
                ans = 0
                while left <= right:
                    mid = (left + right)//2
                    if res[mid] < n:
                        left = mid + 1
                    else:
                        ans = mid
                        right = mid - 1
                # print(n,ans)
                res[ans] = n
        return len(res) >= 3
            