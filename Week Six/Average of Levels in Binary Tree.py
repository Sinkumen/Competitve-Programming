from collections import deque


class Solution:
    def averageOfLevels(self, root):
        queue = deque()
        queue.append(root)
        av = [root.val]
        while queue:
            size = len(queue)
            summ = []
            for _i in range(size):
                current = queue.popleft()
                if current.left:
                    summ.append(current.left.val)
                    queue.append(current.left)
                if current.right:
                    summ.append(current.right.val)
                    queue.append(current.right)

            if len(summ) != 0:
                av.append(sum(summ)/len(summ))
        return av
