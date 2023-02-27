class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                top = ans.pop()
                ans.append((min(top[0],interval[0]),max(top[1],interval[1])))
        return ans