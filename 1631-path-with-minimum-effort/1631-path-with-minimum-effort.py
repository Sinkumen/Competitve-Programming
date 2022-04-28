class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        r = len(heights)-1
        c = len(heights[0])-1
        
        def dfs(pos,k,visited):
            if pos == (r,c):
                return True
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            cur = heights[pos[0]][pos[1]]
            for d in dirs:
                nr = pos[0] + d[0]
                nc = pos[1] + d[1]
                if 0 <= nr <= r and 0 <= nc <= c:
                    nxt = heights[nr][nc]
                    if (nr,nc) not in visited and abs(nxt-cur) <= k:
                        visited.add((nr,nc))
                        res = dfs((nr,nc),k,visited)
                        if res:
                            return True
            return False
        
        start = 0
        end = 10**6
        ans = end
        while start <= end:
            mid = (start + end)//2
            res = dfs((0,0),mid,set((0,0)))
            if res:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
                
                
                        
                    
            