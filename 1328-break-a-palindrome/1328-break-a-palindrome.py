class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        left = 0
        right = len(palindrome)-1
        found = False
        while left < right:
            if palindrome[left] != "a":
                palindrome[left] = "a"
                found = True
                break
            else:
                left += 1
                right -= 1
        if not found:
            palindrome[-1] = "b"
        return "".join(palindrome)