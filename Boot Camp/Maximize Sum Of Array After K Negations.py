class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        for _i in range(K):
            index = A.index(min(A))
            A[index] = -1 * A[index]
        return sum(A)
