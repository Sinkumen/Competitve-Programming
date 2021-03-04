import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))

        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return (-self.maxHeap[0] + self.minHeap[0])/2
