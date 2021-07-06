import heapq
class Solution:
    def minSetSize(self, arr) -> int:
        occ = {}
        for num in arr:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        heap = []
        
        for key,value in occ.items():
            heapq.heappush(heap,(-value,key))
        ans = 1
        tot = -heapq.heappop(heap)[0]
        
        while tot < len(arr)/2:
            tot += -heapq.heappop(heap)[0]
            ans += 1
        return ans