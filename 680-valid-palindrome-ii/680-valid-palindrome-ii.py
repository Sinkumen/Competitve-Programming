class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(left,right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                leftAns = isPalindrom(left,right-1)
                rightAns = isPalindrom(left+1,right)
                return leftAns | rightAns
        return True
        
    
            