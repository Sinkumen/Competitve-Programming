class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        nums = [1]*n
        rem = k - n
        for i in range(n-1,-1,-1):
            rem += 1
            if rem >= 26:
                rem -= 26
                nums[i] = 26
            else:
                nums[i] = max(rem,1)
                break
        ans = []
        for i in range(n):
            ans.append(chr(ord("a") + (nums[i]-1)))
        return "".join(ans)
            
            
                