class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        outgoing = set()
        for node1, node2 in connections:
            outgoing.add((node1, node2))
            graph[node1].add(node2)
            graph[node2].add(node1)

        queue = deque([0])
        visited = {0}
        ans = 0

        while queue:
            current = queue.popleft()
            for neigbor in graph[current]:
                if neigbor not in visited:
                    if (current, neigbor) in outgoing:
                        ans += 1
                    visited.add(neigbor)
                    queue.append(neigbor)

        return ans

        