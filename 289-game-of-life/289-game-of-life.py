class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,1),(1,-1),(-1,-1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                ones  = 0
                zeros = 0
                for d in directions:
                    newI = i + d[0]
                    newJ = j + d[1]
                    if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
                        if abs(board[newI][newJ]) == 1:
                            ones += 1
                        else:
                            zeros += 1
                if board[i][j] == 1:
                    if ones < 2 or ones > 3:
                        board[i][j] = -1
                else:
                    if ones == 3:
                        board[i][j] = -2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1
                    
                
        