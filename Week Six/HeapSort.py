from heapq import heapify, heappop, heappush


class Solution:
    def heap_sort(self, arr):
        res = []
        heapify(arr)
        while arr:
            res.append(heappop(arr))
        return res
