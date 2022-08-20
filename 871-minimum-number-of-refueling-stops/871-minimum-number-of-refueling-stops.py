class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if not stations:
            return 0 if startFuel >= target else -1
        stations.append([target,0])
        heap = []
        startFuel -= stations[0][0] 
        if startFuel < 0:
            return -1
        ans = 0
        for i in range(len(stations)-1):
            
            pos,amount = stations[i]
            diff = stations[i+1][0] - pos
            # print(i,startFuel,amount,diff,heap)
            if startFuel < diff:
                while startFuel < diff and heap:
                    if -heap[0] > amount:  
                        startFuel += -heapq.heappop(heap)
                    else:
                        startFuel += amount
                        amount = 0
                    ans += 1
                if startFuel < diff and amount:
                    startFuel += amount
                    ans += 1
                if startFuel < diff:
                    return -1
                if amount:
                    heapq.heappush(heap,-amount)
            else:
                heapq.heappush(heap,-amount)
            # print(startFuel)
            startFuel -= diff
            # print(startFuel)

        return ans
            
                
                
            
                
            