class Solution:
    def minDays(self, n: int) -> int:
        queue = deque([(n,0)])
        visited = set()
        while queue:
            cur,level = queue.popleft()
            if not cur:
                return level
            if cur-1 not in visited:
                visited.add(cur-1)
                queue.append((cur-1,level+1))
            if cur%2==0 and cur//2 not in visited:
                visited.add(cur//2)
                queue.append((cur//2,level+1))
            if cur%3==0 and ((cur//3)) not in visited:
                visited.add((cur//3))
                queue.append(((cur//3),level+1))
           