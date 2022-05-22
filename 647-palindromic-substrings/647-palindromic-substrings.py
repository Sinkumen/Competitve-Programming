class Solution:
    def countSubstrings(self, s: str) -> int:
        pal = 0
        for i in range(len(s)):
            left = i
            right = i
            ans = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            pal += ans
        return pal
            
                