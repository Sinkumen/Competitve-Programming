class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # if row1 > row2 or col1 > col2:
        #     return
        # self.rectangle[row1][col1] = newValue
        # self.updateSubrectangle(row1+1,col1,row2,col2,newValue)
        # self.updateSubrectangle(row1,col1+1,row2,col2,newValue)
        # return
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
