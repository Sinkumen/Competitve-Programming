class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(x,y):
            nums = []
            cx = x
            cy = y
            
            while 0 <= cx < len(mat) and 0 <= cy < len(mat[0]):
                heapq.heappush(nums,mat[cx][cy])
                cx += 1
                cy += 1
                
            while 0 <= x < len(mat) and 0 <= y < len(mat[0]):
                mat[x][y] = heapq.heappop(nums)
                x += 1
                y += 1
            
        for i in range(len(mat)):
            sort(i,0)
        for j in range(len(mat[0])):
            sort(0,j)
        return mat