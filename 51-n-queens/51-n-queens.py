class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        possible = []
        def disablePath(x,y,val):
            board[x][y] += val
            for i in range(1,n+1):
                if y+i < n: board[x][y+i] += val
                if y-i >= 0: board[x][y-i] += val
                if x+i < n: board[x+i][y] += val
                if x-i >= 0: board[x-i][y] += val
                if y+i < n and x+i < n: board[x+i][y+i] += val
                if y-i >= 0 and x-i >= 0: board[x-i][y-i] += val
                if y-i >= 0 and x+i < n: board[x+i][y-i] += val
                if y+i < n and x-i >= 0: board[x-i][y+i] += val
        ans = []
        def dfs(path,r):
            if len(path) == n:
                ans.append(tuple(path))
                return
            if r < n:
                for j in range(n):
                    if board[r][j] == 0:
                        row = ["." for i in range(n)]
                        row[j] = "Q"
                        disablePath(r,j,-1)
                        path.append("".join(row))
                        dfs(path,r+1)
                        path.pop()
                        disablePath(r,j,1)
        dfs([],0)
        
        return ans
                        
                    
                    