class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [] 
        for i in range(len(mat)):
            cnt = mat[i].count(1)
           
            heapq.heappush(arr,(cnt,i))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(arr)[1])
        return ans
            