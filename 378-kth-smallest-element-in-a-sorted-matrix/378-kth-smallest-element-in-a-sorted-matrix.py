class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(heap,matrix[i][j])
                
        for _i in range(k-1):
            heapq.heappop(heap)
        return heap[0]
        