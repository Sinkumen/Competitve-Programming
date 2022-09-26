class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            while parent[x] != x:
                x,parent[x] = parent[x],parent[parent[x]]
            return x
        
        def union(x,y):
            x = find(x)
            y = find(y)
            if x!=y:
                parent[x] = y
        
        for a,bang,_,b in equations:
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            if bang == '=':
                union(a,b)
                
        for a,bang,_,b in equations:
            if bang == '!' and find(a) == find(b):
                return False
        
        return True