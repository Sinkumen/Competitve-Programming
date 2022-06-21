class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladder: int) -> int:
        heap = []
        step = 0
        
        for i in range(1,len(heights)):
            diff =  heights[i] - heights[i-1]
            if diff <= 0:
                step += 1
            else:
                if ladder:
                    ladder -= 1
                    heapq.heappush(heap,diff)
                    step += 1
                else:
                    if heap and heap[0] < diff:
                        heapq.heappush(heap,diff)
                        diff = heapq.heappop(heap)
                        
                    if bricks >= diff:
                        bricks -= diff
                        step += 1
                    else:
                        break
                
        return step
                    
                    