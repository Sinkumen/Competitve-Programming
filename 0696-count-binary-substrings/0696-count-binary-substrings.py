class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev = "s"
        i = 0
        ans = 0
        while i < len(s):     
            if s[i] != prev:
                # print(i,count,prev,ans)
                temp = i
                while temp < len(s) and count:
                    if s[temp] == prev:
                        break
                    ans += 1
                    count -= 1
                    temp += 1
                prev = s[i]
                count = 0
            else:
                count += 1
                i += 1
        return ans
                
                    
            