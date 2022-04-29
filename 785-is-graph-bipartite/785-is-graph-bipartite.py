class Solution:
    def find(self, p, node):
        while p[node] != p[p[node]]:
            p[node] = p[p[node]]
        return p[node]
    
    def union(self, p, n1, n2):
        p1 = self.find(p, n1)
        p2 = self.find(p, n2)
        p[p1] = p2
        
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        p = [i for i in range(len(graph))]
    
        for i in range(len(graph)):
            for j in graph[i]:
                if self.find(p,i) == self.find(p,j):
                    return False
                for k in graph[j]:
                    self.union(p,i,k)
        return True
                        
        