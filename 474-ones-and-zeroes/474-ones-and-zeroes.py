class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        for s in strs:
            ones = 0
            zeros = 0
            for c in s:
                if c == "1":
                    ones += 1
                else:
                    zeros += 1
            counts.append((zeros,ones))
            
        ans = 0
        @lru_cache(None)
        def dfs(i,count,zeros,ones):
            nonlocal ans
            if i >= len(counts):
                ans = max(ans,count)
                return 
            if zeros + counts[i][0] <= m and ones + counts[i][1] <= n:
                w = dfs(i+1, count+1, zeros + counts[i][0], ones + counts[i][1])
            wo = dfs(i+1, count ,zeros, ones)
        dfs(0,0,0,0)
        return ans