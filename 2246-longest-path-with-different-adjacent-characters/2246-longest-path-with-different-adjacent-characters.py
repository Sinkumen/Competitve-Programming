class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:               
                graph[parent[i]].append(i)
        # print(graph)
        
        def dfs(node):
            cur = 1 
            glb = 1
            for nxt in graph[node]:
                c,g = dfs(nxt)
                # print(node,c,g,s[nxt])
                if not c or s[node] != s[nxt]:
                    two = c + cur 
                    cur = max(cur,c+1)
                    glb = max(glb,g,two)
                else:
                    glb = max(glb,g)
            return (cur,glb)
        return dfs(0)[1]
                
                
