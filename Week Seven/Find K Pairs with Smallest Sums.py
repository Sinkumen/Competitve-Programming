import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        heap = []

        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, (i+j, i, j))
        res = []
        for i in range(k):
            if len(heap):
                val = heapq.heappop(heap)
                res.append([val[1], val[2]])

        return res
