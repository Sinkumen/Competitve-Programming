class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memory = {}

        def dfs(pos):
            if pos in memory:
                return memory[pos]
            row = pos[0]
            col = pos[1]

            if row == m and col == n:
                return 1

            if row != m and col != n:
                right = dfs((row, col+1))
                down = dfs((row+1, col))
                memory[pos] = right + down
                return right + down

            elif col != n:
                right = dfs((row, col+1))
                memory[pos] = right
                return right

            elif row != m:
                down = dfs((row+1, col))
                memory[pos] = down
                return down

        return dfs((1, 1))
