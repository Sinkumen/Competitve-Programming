from collections import deque


class Solution:
    def highestPeak(self, isWater):
        visited = set()
        queue = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    visited.add((i, j))
                    queue.append((i, j))
        while queue:
            row, col = queue.popleft()
            if row+1 < len(isWater) and (row+1, col) not in visited:
                isWater[row + 1][col] = isWater[row][col] + 1
                visited.add((row+1, col))
                queue.append((row+1, col))
            if row-1 >= 0 and (row-1, col) not in visited:
                isWater[row-1][col] = isWater[row][col] + 1
                visited.add((row-1, col))
                queue.append((row-1, col))
            if col + 1 < len(isWater[0]) and (row, col+1) not in visited:
                isWater[row][col+1] = isWater[row][col] + 1
                visited.add((row, col+1))
                queue.append((row, col+1))
            if col - 1 >= 0 and (row, col-1) not in visited:
                isWater[row][col-1] = isWater[row][col] + 1
                visited.add((row, col-1))
                queue.append((row, col-1))

        return isWater
