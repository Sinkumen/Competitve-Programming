class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev = intervals[0]
        ans = 0
        for i in range(1,len(intervals)):
            cur = intervals[i]
            if cur[0] < prev[1]:
                ans += 1
            else:
                prev = cur
        return ans
                
    
        