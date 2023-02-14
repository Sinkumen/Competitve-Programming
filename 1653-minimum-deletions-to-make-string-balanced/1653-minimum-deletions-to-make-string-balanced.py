class Solution:
    def minimumDeletions(self, s: str) -> int:
        pre = [0]

        bcount = 0
        for j in range(len(s)):
            if s[j] == "b":
                bcount += 1
            pre.append(bcount)
        ans = pre[-1] 
        
        acount = 0
        for i in range(len(s)-1,0,-1):
            if s[i]=="a":
                acount += 1
            ans = min(acount + pre[i-1],ans)
        if s[0] == "a":
                acount += 1
        ans = min(acount,ans)

        return ans
                
            
                
                