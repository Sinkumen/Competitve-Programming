class Solution:
    def __init__(self):
        self.visited = set()

    def minTime(self, n: int, edges, hasApple) -> int:
        tree = {}
        for edge in edges:
            if edge[0] not in tree:
                tree[edge[0]] = [edge[1]]
            else:
                tree[edge[0]].append(edge[1])

            if edge[1] not in tree:
                tree[edge[1]] = [edge[0]]
            else:
                tree[edge[1]].append(edge[0])
        print(tree)
        finRes = 0
        count = 0
        for key, _value in tree.items():
            if key not in self.visited:
                count += 1
                curRes = self.dfs(key, tree, hasApple)
                print(curRes)
                finRes += (curRes-2) if curRes > 0 else curRes
        # if count > 1:
        return finRes

    def dfs(self, curr, tree, hasApple):
        if curr in self.visited:
            return 0
        self.visited.add(curr)
        if curr not in tree:
            if hasApple[curr]:
                return 2
            else:
                return 0
        nodes = tree[curr]
        res = 0
        for node in nodes:
            val = self.dfs(node, tree, hasApple)
            res += val
        if res > 0:
            return res + 2
        elif hasApple[curr]:
            return 2
        return 0
