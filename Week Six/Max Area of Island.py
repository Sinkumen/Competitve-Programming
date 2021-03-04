class Solution:
    def __init__(self):
        self.maxArea = 0

    def maxAreaOfIsland(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.maxArea = max(self.maxArea, self.helper(grid, i, j))
        return self.maxArea

    def helper(self, grid, x, y):

        if x >= len(grid) or x < 0 or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0

        grid[x][y] = 0
        area = 1
        area += self.helper(grid, x-1, y)
        area += self.helper(grid, x+1, y)
        area += self.helper(grid, x, y-1)
        area += self.helper(grid, x, y+1)

        return area
