class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(x,y):
            if board[x][y] == "M":
                board[x][y] = "X"
                return
            directions= [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
            bomb = 0
            for dx,dy in directions:
                newX = x+dx
                newY = y+dy
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
                    if board[newX][newY] == "M":
                        bomb += 1
            if bomb:
                board[x][y] = str(bomb)
                return
            
            board[x][y] = "B"
            
            for dx,dy in directions:
                newX = x+dx
                newY = y+dy
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
        
                    if board[newX][newY] == "E":
                        dfs(newX,newY)
        dfs(click[0],click[1])
        return board
                
                
                
                
                    
            
        