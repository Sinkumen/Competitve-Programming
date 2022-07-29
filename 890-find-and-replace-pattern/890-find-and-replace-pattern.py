class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def generate_pattern(word):
            count = 0
            found = {}
            patt = []
            for char in word:
                if char not in found:
                    patt.append(str(count))
                    found[char] = count
                    count += 1
                else:
                    patt.append(str(found[char]))
            return "".join(patt)
        ans = []
        pat = generate_pattern(pattern)
        
        for word in words:
            cur = generate_pattern(word)
            if pat == cur:
                ans.append(word)
        return ans
            