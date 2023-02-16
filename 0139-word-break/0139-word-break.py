class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @lru_cache(None)
        def dfs(left,right):
            word = s[left:right+1]
            if right >= len(s):
                if word in wordDict:
                    return True
                return False
            if word in wordDict and dfs(right + 1,right + 1):
                return True
            return dfs(left,right+1)
        return dfs(0,0)
            
            