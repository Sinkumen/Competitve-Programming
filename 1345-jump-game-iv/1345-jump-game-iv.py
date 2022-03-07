class Solution:
    def minJumps(self, arr: List[int]) -> int:
        occ = defaultdict(list)
        for i in range(len(arr)):
            occ[arr[i]].append(i)
        queue = deque([(0,0)])
        visited = {0}
        while queue:
            cur,level = queue.popleft()
            if cur == len(arr)-1:
                return level
            for n in occ[arr[cur]]:
                if n not in visited:
                    visited.add(n)
                    queue.append((n,level + 1))
            occ[arr[cur]].clear()     
            if (cur - 1) >= 0 and (cur - 1) not in visited:
                visited.add(cur - 1)
                queue.append((cur - 1,level + 1))
                
            if (cur + 1) < len(arr) and (cur + 1) not in visited:
                visited.add(cur + 1)
                queue.append((cur + 1,level + 1))
                
            
            
            
        