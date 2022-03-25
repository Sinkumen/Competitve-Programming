class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[ 10000 for j in range(len(mat[0]))] for i in range(len(mat))]
        visited = set()
        queue = deque()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i,j,0))     
        while queue:
            x,y,level = queue.popleft()
            if mat[x][y] == 1:
                visited.add((x,y))
                ans[x][y] = min(ans[x][y],level)

            for d in dirs:
                nx = x+d[0]
                ny = y+d[1]
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    if (nx,ny) not in visited and mat[nx][ny] == 1:
                        visited.add((nx,ny))
                        queue.append((nx,ny,level+1))
                            
        return ans
        