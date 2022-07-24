class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(isrow,row):
            left = 0
            right = len(matrix[0])-1 if isrow else len(matrix)-1
            if isrow:
                while left <= right:
                    mid = (left + right)//2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            else:
                ans = -1
                while left <= right:
                    mid = (left + right)//2

                    if matrix[mid][0] == target:
                        return mid
                    elif matrix[mid][0] > target:
                        right = mid - 1
                    else:
                        ans = mid
                        left = mid + 1
                return ans
        row = binary(False,0)
        if row == -1:
            return False
        for i in range(row+1):
            if binary(True,i):
                return True
        return False
                
                