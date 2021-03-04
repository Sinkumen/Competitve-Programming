from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = [[root.val]]
        lev = 2
        while queue:
            size = len(queue)
            level = []
            for _i in range(size):
                current = queue.popleft()
                if current.left:
                    level.insert(0, current.left.val) if lev % 2 == 0 else level.append(
                        current.left.val)
                    queue.append(current.left)
                if current.right:
                    level.insert(0, current.right.val) if lev % 2 == 0 else level.append(
                        current.right.val)
                    queue.append(current.right)
            lev += 1
            if len(level) != 0:
                res.append(level)
        return res
