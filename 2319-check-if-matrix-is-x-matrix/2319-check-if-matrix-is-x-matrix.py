class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        for i in range(len(grid)):
            if grid[i][i] == 0 or grid[i][len(grid)-i-1] == 0:
                return False
            grid[i][i] = grid[i][len(grid)-i-1] = -1
            
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[j][k] != -1 and grid[j][k] != 0:
                    return False
        return True