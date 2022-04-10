class Solution:
    def longestPalindrome(self, s: str) -> str:
        width = 1
        l = 0
        r = 0
        for i in range(len(s)):
            left = i 
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > width:
                    l = left
                    r = right
                    width = (right - left + 1)
                left -= 1
                right += 1
            left = i 
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > width:
                    l = left
                    r = right
                    width = right - left + 1
                left -= 1
                right += 1
        return s[l:r+1]
            
                    
                
                    