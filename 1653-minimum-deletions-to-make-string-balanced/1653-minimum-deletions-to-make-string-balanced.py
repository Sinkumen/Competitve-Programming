class Solution:
    def minimumDeletions(self, s: str) -> int:
        pre = []
        suf = [0 for _ in range(len(s))]
        firstB = 0
        acount = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "b":
                firstB = i
            else:
                acount += 1
            suf[i] = acount

        lastA = 0
        bcount = 0
        for j in range(len(s)):
            if s[j] == "a":
                lastA = j
            else:
                bcount += 1
            pre.append(bcount)
        ans = min(suf[0],pre[-1])
        for k in range(1,len(s)):
            ans = min(suf[k] + pre[k-1],ans)
        return ans
                
            
                
                