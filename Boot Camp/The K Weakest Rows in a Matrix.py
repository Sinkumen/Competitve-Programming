import heapq


class Solution:
    def kWeakestRows(self, mat, k: int):
        heap = []
        for i in range(len(mat)):
            row = mat[i]
            soldiers = 0
            for col in row:
                if col == 1:
                    soldiers += 1
                else:
                    break
            heapq.heappush(heap, (soldiers, i))
        res = []
        prev = None
        for _i in range(k):
            cur = heapq.heappop(heap)
            if not res:
                res.append(cur[1])
                prev = cur[0]
            else:
                if prev == cur[0] and cur[1] < res[-1]:
                    res.insert(cur[-2])
                else:
                    res.append(cur[1])
                    prev = cur[0]

        return res
