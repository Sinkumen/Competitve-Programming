class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = ""
        prevCost = 0  
        ans = 0
        for i in range(len(colors)):
            if colors[i] == prev:
                ans += min(neededTime[i],prevCost)
                prevCost = max(neededTime[i],prevCost)
            else:
                prev = colors[i]
                prevCost = neededTime[i]
        return ans