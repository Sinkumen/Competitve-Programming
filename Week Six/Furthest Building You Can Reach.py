import heapq


class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        steps = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) <= ladders:
                steps += 1
            else:
                last = heapq.heappop(heap)
                if last > bricks:
                    break
                else:
                    bricks -= last
                    steps += 1

        return steps
