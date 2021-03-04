import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -stone)

        while(len(heap) > 1):
            top = -heapq.heappop(heap)
            nextTop = -heapq.heappop(heap)

            if top != nextTop:
                heapq.heappush(heap, -(top - nextTop))

        return -heap[0] if len(heap) == 1 else 0
