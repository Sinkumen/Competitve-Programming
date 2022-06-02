class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))] 
        print(ans)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]
        return ans