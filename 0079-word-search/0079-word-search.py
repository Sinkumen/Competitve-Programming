class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,x,y):
            if i == len(word)-1:
                if board[x][y] == word[i]:
                    return True
                return False
            for d in directions:
                nx = x + d[0]
                ny = y + d[1]
                if 0<=nx<len(board) and 0<=ny<len(board[0]):
                    if (nx,ny) not in visited and board[nx][ny] == word[i+1]:
                        visited.add((nx,ny))
                        if dfs(i+1,nx,ny):
                            print(i+1,nx,ny)
                            return True
                        visited.remove((nx,ny))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if dfs(0,i,j):
                        return True
                    visited.remove((i,j))

        
        return False
            