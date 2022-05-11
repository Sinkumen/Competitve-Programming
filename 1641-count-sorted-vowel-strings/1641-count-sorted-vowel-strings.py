class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = 0
        vowels = ["a","e","i","o","u"]
        def dfs(k,last):
            nonlocal ans
            if k > n:
                ans += 1
                return
            
            for i in range(last,len(vowels)):
                dfs(k+1,i)
        dfs(1,0)
        return ans
            