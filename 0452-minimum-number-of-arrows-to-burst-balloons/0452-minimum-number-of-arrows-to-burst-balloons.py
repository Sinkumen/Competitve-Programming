class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        ans,last = 0,float("-inf")
        for s,e in points:
            if s > last:
                ans += 1
                last = e
            else:
                last = min(last,e)
        return ans
            
            