class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = ""
        heap = []
        ans = 0
        for i in range(len(colors)):
            while colors[i] != prev and len(heap) > 1:
                ans += heapq.heappop(heap)
            if colors[i] != prev: heap = []
            heapq.heappush(heap,neededTime[i])
            prev = colors[i]
        while len(heap) > 1:
            ans += heapq.heappop(heap)
        return ans