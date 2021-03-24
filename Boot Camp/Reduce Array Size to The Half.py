import heapq


class Solution:
    def minSetSize(self, arr) -> int:
        occ = {}
        heap = []
        for num in arr:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1

        for _key, value in occ.items():
            heapq.heappush(heap, -value)

        summ = -heapq.heappop(heap)
        count = 1
        while summ < len(arr)/2:
            summ += -heapq.heappop(heap)
            count += 1
        return count
