class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        def dfs(i,j,cur):
            word = s[i:j+1] 
            if j >= len(s):
                if word in wordDict:
                    cur.append(word)
                    ans.append(" ".join(cur))
                    cur.pop()
                return
            
            dfs(i,j+1,cur)
            if word in wordDict:
                cur.append(word)
                dfs(j+1,j+1,cur)
                cur.pop()
            return
        dfs(0,0,[])
        return ans
            
            
                    