from heapq import heappop, heappush


class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        q = []
        for i in range(len(classes)):
            pas, tot = float(classes[i][0]), float(classes[i][1])
            val = (pas+1.0)/(tot+1.0)-pas/tot
            heappush(q, (-val, pas, tot))
        for i in range(extraStudents):
            val, pas, tot = heappop(q)
            pas += 1.0
            tot += 1.0
            val = (pas+1.0)/(tot + 1.0) - pas/tot
            heappush(q, (-val, pas, tot))
        s = 0.0
        for i in range(len(classes)):
            val, pas, tot = heappop(q)
            # print(pas,tot)
            s += pas/tot
        return s/len(classes)
