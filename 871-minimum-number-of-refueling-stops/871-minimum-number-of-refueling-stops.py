class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        stations.append([target,0])
        heap = []
        startFuel -= stations[0][0] 
        if startFuel < 0:
            return -1
        ans = 0
        
        for i in range(len(stations)-1):
            pos,amount = stations[i]
            heapq.heappush(heap,-amount)
            diff = stations[i+1][0] - pos
            if startFuel < diff:
                while startFuel < diff and heap:
                    startFuel += -heapq.heappop(heap)
                    ans += 1

                if startFuel < diff:
                    return -1
   
            startFuel -= diff

        return ans
            
                
                
            
                
            