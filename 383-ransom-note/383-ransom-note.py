class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        for key in rc.keys():
            if key not in mc or rc[key] > mc[key]:
                return False
        return True