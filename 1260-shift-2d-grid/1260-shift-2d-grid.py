class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(grid):
            n = len(grid)-1
            m = len(grid[0])-1

            prev = grid[n][m]
            for i in range(n+1):
                temp = grid[i][m]
                for j in range(m,0,-1):
                    grid[i][j] = grid[i][j-1]
                grid[i][0] = prev
                prev = temp
            return grid
        for i in range(k):
            shift(grid)
        return grid
            
            
                
                
                    