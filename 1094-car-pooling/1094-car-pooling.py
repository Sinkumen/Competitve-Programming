class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        # print(trips)
        left = 0
        right = 0
        passengers = 0
        prevs = []
        while right < len(trips):
            cur,start,end = trips[right]
            while prevs and prevs[0][0] <= start:
                passengers -= heapq.heappop(prevs)[1]
            if cur + passengers > capacity:
                return False
            heapq.heappush(prevs,(end,cur))
            passengers += cur
            right += 1
        return True
       