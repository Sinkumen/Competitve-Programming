class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    fresh += 1
        if not fresh and not queue:
            return 0
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 0
        while queue:
            x,y,level = queue.popleft()
            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 1:
                    grid[newX][newY] = 2
                    count += 1
                    queue.append((newX,newY,level+1))
        return level if count == fresh else -1
                