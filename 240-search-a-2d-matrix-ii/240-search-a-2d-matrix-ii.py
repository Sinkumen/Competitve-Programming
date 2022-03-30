class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        def searchRow(row):
            start = 0
            end = len(mat[row])-1
            while start <= end:
                mid = (start+end)//2
                if mat[row][mid] == target:
                    return True
                elif mat[row][mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False
        for i in range(len(mat)):
            res = searchRow(i)
            if res:
                return True
        return False
       