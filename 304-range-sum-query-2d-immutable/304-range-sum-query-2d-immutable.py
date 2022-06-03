class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                if i-1 >= 0 and j-1 >= 0:
                    self.matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]
                    self.matrix[i][j] -= matrix[i-1][j-1] 
                elif i-1 >= 0:
                    self.matrix[i][j] += matrix[i-1][j]
                elif j-1 >= 0:
                    self.matrix[i][j] += matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2]
        if row1-1 >= 0 and col1-1 >= 0:
            ans -= self.matrix[row1 - 1][col2] + self.matrix[row2][col1-1]
            ans += self.matrix[row1 - 1][col1-1]
        elif row1-1 >= 0:
            ans -= self.matrix[row1-1][col2]
        elif col1-1 >= 0:
            ans -= self.matrix[row2][col1-1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)