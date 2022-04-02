class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                leftAns = self.isPalindrom(s[left:right])
                rightAns = self.isPalindrom(s[left+1:right+1])
                return leftAns | rightAns
        return True
        
    def isPalindrom(self,s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            