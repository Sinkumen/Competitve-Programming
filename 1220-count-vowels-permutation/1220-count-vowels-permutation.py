class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        nextVowel = {"a":["e"],"e":["a","i"],"i":["a","e","o","u"],"o":["i","u"],"u":["a"]}
        @lru_cache(None)
        def dfs(i,vowel):
            if vowel not in nextVowel:
                res = 0
                for nxt in nextVowel.keys():
                    res += dfs(i+1,nxt)
                return res
           
            if i == n:
                return 1
            res = 0
            for nxt in nextVowel[vowel]:
                res += dfs(i+1,nxt)
            return res
        return dfs(0,"b")%mod
                