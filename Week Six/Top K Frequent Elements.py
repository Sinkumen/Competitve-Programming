import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        heap = []
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for key, value in dict.items():
            heapq.heappush(heap, (-value, key))
        ans = []
        for _i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
