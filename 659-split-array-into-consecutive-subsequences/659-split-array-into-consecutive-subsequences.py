class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        temp = {}
        for n in nums:
            if n not in temp:
                temp[n] = []
            if n-1 in temp and temp[n-1]:
                top,level = heapq.heappop(temp[n-1])
                heapq.heappush(temp[n],(n,level+1))
            else:
                heapq.heappush(temp[n],(n,1))

        for heap in temp.keys():            
            if temp[heap] and temp[heap][0][1] < 3 :
                return False
        return True
                    