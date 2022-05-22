class Solution:
    def countSubstrings(self, s: str) -> int:
        def pals(left,right):
            ans = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            return ans
        pal = 0
        for i in range(len(s)):
            pal += pals(i,i)
            pal += pals(i,i+1)
        return pal
            
                