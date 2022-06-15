class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
        def check(pre,nxt):
            if len(nxt) - len(pre) != 1:
                return False
            p = 0
            n = 0
            while p < len(pre) and n < len(nxt):
                if pre[p] == nxt[n]:
                    p += 1
                    n += 1
                else:
                    n += 1
            if p < len(pre):
                return False
            return True
        
        dp = [1]*len(words)
        for i in range(len(words)-1,-1,-1):
            for j in range(i+1,len(words)):
                if check(words[i],words[j]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
            
                
                