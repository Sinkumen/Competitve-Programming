import heapq


class Solution:
    def topKFrequent(self, words, k: int):
        if len(words) == 0:
            return []
        heap = []
        frequency = {}

        for i in words:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        for key, value in frequency.items():
            heapq.heappush(heap, (-value, key))

        return [heapq.heappop(heap)[1] for i in range(k)]
