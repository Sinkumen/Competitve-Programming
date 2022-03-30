class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        def findRow():
            start = 0
            end = len(mat)-1
            row = -1
            while start <= end:
                mid = (start+end)//2
                if mat[mid][0] == target:
                    return mid
                elif mat[mid][0] < target:
                    row = mid
                    start = mid + 1
                else:
                    end = mid - 1
            return row
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
        row = findRow()
        return searchRow(row)
                
            
                