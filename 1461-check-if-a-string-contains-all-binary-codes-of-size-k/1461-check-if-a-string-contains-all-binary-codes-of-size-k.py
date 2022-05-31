class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found = set()
        left = 0
        right = k-1
        while right < len(s):
            found.add(s[left:right+1])
            right += 1
            left += 1
        return len(found) >= 2**k