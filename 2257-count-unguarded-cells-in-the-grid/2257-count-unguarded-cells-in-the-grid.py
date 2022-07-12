class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set([tuple(g) for g in guards])
        walls = set([tuple(w) for w in walls])
        ng = set()
        def guard(x,y):
            ng.add((x,y))
            cur = x+1
            while cur < m and (cur,y) not in guards and (cur,y) not in walls:
                ng.add((cur,y))
                cur += 1
            cur = x-1
            while 0 <= cur and (cur,y) not in guards and (cur,y) not in walls:
                ng.add((cur,y))
                cur -= 1
                
            cur = y-1
            while 0 <= cur and (x,cur) not in guards and (x,cur) not in walls:
                ng.add((x,cur))
                cur -= 1
            cur = y+1
            while  cur < n and (x,cur) not in guards and (x,cur) not in walls:
                ng.add((x,cur))
                cur += 1
            
        for i in range(m):
            for j in range(n):
                if (i,j) in guards:
                    guard(i,j)

        
        return (m*n)-(len(ng)+len(walls))
                    