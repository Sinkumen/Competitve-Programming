class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = []
        for interval in intervals:
            if not groups or groups[0] >= interval[0]:
                heapq.heappush(groups,interval[1])
            else:
                heapq.heappop(groups)
                heapq.heappush(groups,interval[1])
        return len(groups)
            