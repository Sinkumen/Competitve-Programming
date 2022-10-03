class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(heap,(dist,point))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans