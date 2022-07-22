class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        z = len(board[0])
        n = len(word)
        def is_valid(i,j)->bool:
            return 0 <= i < m and 0 <= j < z
        def dfs(i, j, k):
            if k == n or (k+1 == n and word[k] == board[i][j] and board[i][j]):
                return True
            DIR = (1, 0, -1, 0, 1)
            for ii in range(4):
                r, c = i+DIR[ii], j+DIR[ii+1]
                if is_valid(r,c) and board[r][c] == word[k] and board[r][c]:
                    temp, board[r][c] = board[r][c], 0
                    if dfs(r, c, k+1):
                        return True
                    board[r][c] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp, board[i][j] = board[i][j],0
                    if dfs(i,j,1):
                        return True
                    board[i][j]=temp
        return False