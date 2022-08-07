class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curTime = 0
        counts = Counter(tasks)
        heap = []
        for key,val in counts.items():
            heapq.heappush(heap,(-val,key))
        last = {}
        while heap:
            if heap[0][1] not in last:
                rem,task = heapq.heappop(heap)
                rem += 1
                if rem:
                    heapq.heappush(heap,(rem,task))
                last[task] = curTime
                curTime += 1
            else:
                temp = []
                while heap and heap[0][1] in last and (curTime-last[heap[0][1]]-1) < n:
                    temp.append(heapq.heappop(heap))

                if not heap:
                    rem,task = temp[0]
                    diff = (curTime-last[task]-1)
                    curTime += (n - diff)
                    rem += 1
                    if rem:
                        heapq.heappush(heap,(rem,task))
                    last[temp[0][1]] = curTime
                    for j in range(1,len(temp)):
                        heapq.heappush(heap,temp[j])
                else:
                    rem,task = heapq.heappop(heap)
                    rem += 1
                    if rem:
                        heapq.heappush(heap,(rem,task))
                    last[task] = curTime
                    for j in range(len(temp)):
                        heapq.heappush(heap,temp[j])
                curTime += 1
                
                
        return curTime
                
                
                
                
                
                
            
            
            