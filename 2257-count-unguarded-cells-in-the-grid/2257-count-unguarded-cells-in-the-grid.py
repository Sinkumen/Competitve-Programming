class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set([tuple(g) for g in guards])
        walls = set([tuple(w) for w in walls])
        ng = set()
        def guard(x,y):
            ng.add((x,y))
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            
            for direc in directions:
                nx = x + direc[0]
                ny = y + direc[1]
                while 0<= nx < m and 0<= ny < n and (nx,ny) not in guards and (nx,ny) not in walls:
                    ng.add((nx,ny))
                    nx += direc[0]
                    ny += direc[1]
           
            
        for i in range(m):
            for j in range(n):
                if (i,j) in guards:
                    guard(i,j)

        
        return (m*n)-(len(ng)+len(walls))
                    