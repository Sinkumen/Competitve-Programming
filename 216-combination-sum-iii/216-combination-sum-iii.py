class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        visited = set()
        def dfs(i,summ,res):
            
            if i > k or summ > n:
                return
            if summ == n and i==k:
                srtd = sorted(res)
                tup = tuple(srtd)
                if tup not in visited:
                    visited.add(tup)
                    ans.append(srtd)
                return
            for j in range(i+1,10):
                if j not in res:
                    res.add(j)
                    dfs(i+1,summ+j,res)
                    res.remove(j)
        dfs(0,0,set())
        return ans