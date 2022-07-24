class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(row):
            left = 0
            right = len(matrix[0])-1 
            while left <= right:
                mid = (left + right)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for i in range(len(matrix)):
            if matrix[i][0] <= target and binary(i):
                return True
        return False
                
                