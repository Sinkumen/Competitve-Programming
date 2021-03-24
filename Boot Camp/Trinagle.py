class Solution:
    def minimumTotal(self, triangle) -> int:
        memory = {}

        def dfs(pos):
            nonlocal memory
            row = pos[0]
            col = pos[1]

            if row == len(triangle)-1:
                memory[pos] = triangle[row][col]
                return triangle[row][col]

            left = dfs((row+1, col)) if (row+1,
                                         col) not in memory else memory[(row+1, col)]
            right = dfs((row+1, col+1)) if (row+1, col +
                                            1) not in memory else memory[(row+1, col+1)]
            memory[pos] = min(left, right) + triangle[row][col]

            return min(left, right) + triangle[row][col]

        return dfs((0, 0))
