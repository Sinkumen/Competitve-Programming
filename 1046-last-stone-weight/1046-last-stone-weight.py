import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first, two = -heapq.heappop(stones),-heapq.heappop(stones)
            if first != two:
                heapq.heappush(stones,-(first-two))
        return abs(stones[0]) if stones else 0
        