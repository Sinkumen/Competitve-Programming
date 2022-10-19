class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        freq = []
        for key,val in count.items():
            heapq.heappush(freq,(-val,key))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(freq)[1])
        return ans