"""
[
[1, 1, 2], 
[1, -1, 3]]

"""
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n,m = len(matrix),len(matrix[0])
        
        if n > m:
            matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]
            n,m = m,n
        
        cumcolsums = [[0 for j in range(m)] for i in range(n+1)]
        
        
        for j in range(m):
            for i in range(n+1):
                if i > 0: cumcolsums[i][j]=cumcolsums[i-1][j]+matrix[i-1][j]
            
        
        curbest = -float('inf')
        for li in range(n):
            for ri in range(li,n):
                cumcols = 0
                colssorted = [0]
                for j in range(m):
                    cumcols+=cumcolsums[ri+1][j] - cumcolsums[li][j]
                    #want: cumcols - target <= k --> cumcols <= target + k
                    target = cumcols-k
                    i = bisect.bisect_left(colssorted,target)
                    if i == len(colssorted) and colssorted[i-1] == target:
                        return k
                    elif i<len(colssorted):
                        curbest = max(curbest,cumcols-colssorted[i])
                    
                    bisect.insort(colssorted,cumcols)
                    
        return curbest