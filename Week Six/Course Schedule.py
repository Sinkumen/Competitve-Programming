from collections import deque


class Solution:
    def __init__(self):
        self.res = []

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not len(prerequisites):
            return True

        incomingEdges = [0]*numCourses
        graph = {}
        for pre in prerequisites:
            parent = pre[1]
            child = pre[0]
            incomingEdges[child] += 1
            if parent not in graph:
                graph[parent] = [child]
            else:
                graph[parent].append(child)

        queue = deque()

        if 0 in incomingEdges:
            for i in range(len(incomingEdges)):
                if incomingEdges[i] == 0:
                    queue.append(i)
            print(incomingEdges.index(0))
        else:
            return False
        res = []
        while queue:
            current = queue.popleft()
            res.append(current)
            if current in graph:
                for ch in graph[current]:
                    incomingEdges[ch] -= 1
                    if incomingEdges[ch] == 0:
                        queue.append(ch)
        return len(res) == numCourses
