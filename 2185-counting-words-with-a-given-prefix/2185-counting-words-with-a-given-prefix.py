class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        ans = 0
        for word in words:
            if word[:n] == pref: ans += 1
        return ans