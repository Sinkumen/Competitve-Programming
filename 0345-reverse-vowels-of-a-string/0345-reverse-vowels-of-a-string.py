class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["A","O","I","U","E","a","o","u","i","e"])
        s = list(s) 
        left  = 0
        right = len(s)-1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            elif s[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)
                