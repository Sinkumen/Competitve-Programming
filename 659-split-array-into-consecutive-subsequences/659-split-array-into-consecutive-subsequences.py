class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        temp = [[] for i in range(2002)]
        for n in nums:
            offset = n + 1000
            if offset and temp[offset-1]:
                top,level = heapq.heappop(temp[offset-1])
                heapq.heappush(temp[offset],(offset,level+1))
            else:
                heapq.heappush(temp[offset],(offset,1))
        
        for heap in temp:            
            if heap and heap[0][1] < 3 :
                return False
        return True
                    