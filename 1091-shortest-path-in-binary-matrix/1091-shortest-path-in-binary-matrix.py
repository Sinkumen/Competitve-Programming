class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        queue = deque([])
        if grid[0][0] == 0:
            queue.append((0,0,1))
        visited = set()
        while queue:
            x,y,level = queue.popleft()
            if x == len(grid)-1 and y == len(grid[0])-1:
                return level
            for d in dirs:
                nx = x+d[0]
                ny = y+d[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 0 and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny,level+1))
        return -1