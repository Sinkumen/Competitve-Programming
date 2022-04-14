class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)] for j in range(n)]
        visited = set([(0,0)])
        def fill(x,y,val,lastMove):
            mat[x][y] = val
            if lastMove == "R":
                if y < n-1 and (x,y+1) not in visited:
                    visited.add((x,y+1))
                    fill(x,y+1,val+1,"R")
                elif x < n-1 and (x+1,y) not in visited:
                    visited.add((x+1,y))
                    fill(x+1,y,val+1,"D")
            if lastMove == "D":
                if x < n-1 and (x+1,y) not in visited:
                    visited.add((x+1,y))
                    fill(x+1,y,val+1,"D")
                elif y > 0 and (x,y-1) not in visited:
                    visited.add((x,y-1))
                    fill(x,y-1,val+1,"L")
            if lastMove == "L":
                if y > 0 and (x,y-1) not in visited:
                    visited.add((x,y-1))
                    fill(x,y-1,val+1,"L")
                elif x > 0 and (x-1,y) not in visited:
                    visited.add((x-1,y))
                    fill(x-1,y,val+1,"U")
            if lastMove == "U":
                if x > 0 and (x-1,y) not in visited:
                    visited.add((x-1,y))
                    fill(x-1,y,val+1,"U")
                elif y < n-1 and (x,y+1) not in visited:
                    visited.add((x,y+1))
                    fill(x,y+1,val+1,"R")    
        fill(0,0,1,"R")
        return mat