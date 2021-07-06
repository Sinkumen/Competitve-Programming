class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        total = m * n
        ans = []
        if total % c != 0:
            return mat
        
        if total/c != r:
            return mat
        cur = []
        for row in mat:
            for i in row:
                if len(cur) < c:
                    cur.append(i)
                if len(cur) == c :
                    ans.append(cur)
                    cur = []
        return ans
        