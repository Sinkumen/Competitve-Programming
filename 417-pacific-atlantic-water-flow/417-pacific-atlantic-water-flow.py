"""
[
[1,1],
[1,1],
[1,1]]
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        def dfs(x,y,isPacific,visited):
            if isPacific:
                pacific.add((x,y))
            else:
                atlantic.add((x,y))
                
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]
                if 0<=newX<len(heights) and 0<=newY<len(heights[0]):
                    if (newX,newY) not in visited and heights[x][y] <= heights[newX][newY]:
                        visited.add((newX,newY))
                        dfs(newX,newY,isPacific,visited)
                    
        avisited = set()
        pvisited = set()
        for i in range(len(heights[0])):
            pvisited.add((0,i))
            avisited.add((len(heights)-1,i))
            dfs(0,i,True,pvisited)
            dfs(len(heights)-1,i,False,avisited)
        for j in range(len(heights)):
            pvisited.add((j,0))
            avisited.add((j,len(heights[0])-1))
            dfs(j,0,True,pvisited)
            dfs(j,len(heights[0])-1,False,avisited)
        ans = []
        # print(avisited)
        # print(pvisited)
        for a in avisited:
            if a in pvisited:
                ans.append(a)
        return ans

            