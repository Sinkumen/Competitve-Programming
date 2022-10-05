class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def findSum(l,r,t,b):
            total = 0
            for i in range(t,b+1):
                for j in range(l,r+1):
                    total += grid[i][j]
            total -= (grid[t+1][l] + grid[t+1][r])
            return total
        ans = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                # print(i,j)
                # print(findSum(j,j+2,i,i+2))
                ans = max(ans,findSum(j,j+2,i,i+2))
        return ans
        