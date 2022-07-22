class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,x,y):
            if i == len(word)-1:
                if board[x][y] == word[i]:
                    return True
                return False
            direcs = [(0,1),(1,0),(-1,0),(0,-1)]
            for direc in direcs:
                nx = x + direc[0]
                ny = y + direc[1]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    board[x][y] = "*"
                    if board[nx][ny] == word[i+1] and dfs(i+1,nx,ny):
                        return True
                    board[x][y] = word[i]
                    
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(0,i,j):
                    return True
        return False
                    