class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        if len(s) == 1: return False

        factors = []
        n = 1
        while n <= len(s)/2:
            if len(s)%n == 0: factors.append(n)
            n += 1
        for window in factors:
            left = 0
            right = window

            while right + window <= len(s) and s[left:left+window] == s[right:right+window]:
                left += window
                right += window

            if right >= len(s):
                return True
            
        return False