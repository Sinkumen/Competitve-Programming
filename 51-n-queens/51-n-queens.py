class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        possible = set()
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
       
        def dfs(path,r):
            if len(path) == n:
                possible.add(tuple(sorted(path)))
                return
            if r < n:
                for j in range(n):
                    if board[r][j] == 0:
                        disablePath(r,j,-1)
                        path.append((r,j))
                        dfs(path,r+1)
                        path.pop()
                        disablePath(r,j,1)
        dfs([],0)
        ans = []
        # print(possible)
        for poss in possible:
            final = [["." for _ in range(n)] for _ in range(n)]
            res = []
            for x,y in poss:
                final[x][y] = "Q"
            for row in final:
                res.append("".join(row))
            ans.append(res)
        return ans
                        
                    
                    