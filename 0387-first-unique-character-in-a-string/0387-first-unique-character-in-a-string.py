class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [0 for _ in range(26)]
        for char in s:
            idx = ord(char) - ord("a")
            chars[idx] += 1
        for i in range(len(s)):
            if chars[ord(s[i]) - ord("a")] == 1:
                return i
        return -1