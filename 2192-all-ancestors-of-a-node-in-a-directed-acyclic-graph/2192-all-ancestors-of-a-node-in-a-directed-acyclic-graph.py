class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incomming = [0]*n
        ancestors = defaultdict(set)
        out = defaultdict(list)
        for edge in edges:
            out[edge[0]].append(edge[1])
        for edge in edges:
            incomming[edge[1]] += 1
        queue = deque()
        for i in range(n):
            if incomming[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.pop()
            for nxt in out[cur]:
                ancestors[nxt].add(cur)
                if cur in ancestors:
                    ancestors[nxt] = ancestors[nxt].union(ancestors[cur])
                incomming[nxt] -= 1
                if not incomming[nxt]:
                    queue.append(nxt)
        ans = []
        for i in range(n):
            if i in ancestors:
                ans.append(sorted(ancestors[i]))
            else:
                ans.append([])
        return ans
                
            
        
            
        