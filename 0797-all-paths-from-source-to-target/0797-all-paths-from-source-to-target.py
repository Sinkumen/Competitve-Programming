class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(i,res):
            if i == len(graph)-1:
                ans.append(res.copy())
            
            for nxt in graph[i]:
                res.append(nxt)
                dfs(nxt,res)
                res.pop()
        dfs(0,[0])
        return ans
            
        