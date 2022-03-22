class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ["a"]*n
        rem = k - n
        for i in range(n-1,-1,-1):
            rem += 1
            if rem >= 26:
                rem -= 26
                ans[i] = "z"
            else:
                c = chr(ord("a") + (max(rem,1)-1))
                ans[i] = c
                break
        return "".join(ans)
            
            
                