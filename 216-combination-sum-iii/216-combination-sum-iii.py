class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        visited = set()
        def dfs(i,summ,res):
            if len(res) == k :
                if summ == n:
                    ans.append(sorted(res))
                return

            for j in range(i+1,10):
                if j <= n:
                    dfs(j,summ+j,res+[j])
                else:
                    return
        dfs(0,0,[])
        return ans