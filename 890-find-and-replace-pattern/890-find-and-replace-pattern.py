class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        ans = []
        
        for word in words:
    
            dic = dict()
            seen = set()
            found = True
            for j in range(len(pattern)):
                if pattern[j] not in dic:
                    if word[j] not in seen:
                        dic[pattern[j]] = word[j]
                        seen.add(word[j])
                    else:
                        found = False
                        break
                elif dic[pattern[j]] != word[j]:
                    found = False
                    break
            if found:
                ans.append(word)
        return ans
                