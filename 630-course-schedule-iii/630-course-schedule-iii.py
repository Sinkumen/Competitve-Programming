class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        maxheap = []
        currentDay = 0
        courses.sort(key = lambda x:x[1])
        
        for duration, lastDay in courses:
            currentDay += duration
            heapq.heappush(maxheap,-duration)
            if currentDay > lastDay:
                currentDay += heapq.heappop(maxheap)

        return len(maxheap)
        