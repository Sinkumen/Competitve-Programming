class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
            
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if j == k or k == len(grid)-j-1:
                    if grid[j][k] == 0:
                        return False
                elif grid[j][k] != 0:
                    return False
        return True