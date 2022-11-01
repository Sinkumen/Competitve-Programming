class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        ans = []
        heap = []
        while right < len(nums):
            if right >= k:
                while heap and heap[0][1] < left:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
                left += 1
            heapq.heappush(heap,(-nums[right],right))
            right += 1
        while heap and heap[0][1] < left:
            heapq.heappop(heap)
        ans.append(-heap[0][0])
        return ans
                
            