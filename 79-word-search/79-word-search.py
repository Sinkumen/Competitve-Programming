class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = self.dfs((i,j),0,board,word,set([(i,j)]))
                    if res:
                        return True
        return False
    def dfs(self,pos,level,board,word,visited):
        if level == len(word)-1:
            return True
        x,y = pos
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for d in directions:
            newX = x+d[0]
            newY = y+d[1]
            if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
                if (board[newX][newY] == word[level+1]) and (newX,newY) not in visited:
                    visited.add((newX,newY))
                    res = self.dfs((newX,newY),level+1,board,word,visited)
                    if res:
                        return True
                    visited.remove((newX,newY))
        return False