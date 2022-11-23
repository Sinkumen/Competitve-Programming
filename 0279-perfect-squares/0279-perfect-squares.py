class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i**2 <= n:
            squares.append(i**2)
            i += 1
        squares = squares[::-1]
        queue = deque([(0,0)]) 
        visited = set()
        while queue:
            cur,level = queue.popleft()
            if cur == n:
                return level
            for sq in squares:
                if cur+sq <= n and cur+sq not in visited:
                    visited.add(cur+sq)
                    queue.append((cur+sq,level+1))
