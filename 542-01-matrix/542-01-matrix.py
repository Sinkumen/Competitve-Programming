class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    val = 10000
                    if i > 0:
                        val = min(val,mat[i-1][j])
                    if j > 0:
                        val = min(val,mat[i][j-1])
                    mat[i][j] = val + 1
             
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j] != 0:
                    val = 10000
                    if i < len(mat)-1:
                        val = min(val,mat[i+1][j])
                    if j < len(mat[0])-1:
                        val = min(val,mat[i][j+1])
                    mat[i][j] = min(mat[i][j],val + 1)  
        return mat
        