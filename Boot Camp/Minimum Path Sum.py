class Solution:
    def minPathSum(self, grid) -> int:
        memory = {}

        def dfs(pos):
            nonlocal memory
            if pos in memory:
                return memory[pos]

            row = pos[0]
            col = pos[1]
            curCell = grid[row][col]
            if row == len(grid)-1 and col == len(grid[0])-1:
                memory[pos] = curCell
                return curCell
            if row != len(grid)-1 and col != len(grid[0])-1:
                down = dfs((row+1, col))
                right = dfs((row, col+1))
                memory[pos] = min(down, right)+curCell
                return min(down, right)+curCell
            elif row != len(grid)-1:
                down = dfs((row+1, col))
                memory[pos] = down+curCell
                return down+curCell

            elif col != len(grid[0])-1:
                right = dfs((row, col+1))
                memory[pos] = right+curCell
                return right+curCell

        return dfs((0, 0))
