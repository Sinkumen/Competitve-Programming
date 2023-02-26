class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = []
        used = []
        free = []
        for i in range(n):
            rooms.append(0)
            free.append(i)
        mx = 0
        for meet in meetings:
            diff = meet[1] - meet[0]
            if not used:
                room = heapq.heappop(free)
                heapq.heappush(used,(meet[1],room))
                rooms[room] += 1
                mx = max(mx,rooms[room])
            else:
                while used and used[0][0] <= meet[0]:
                    top = heapq.heappop(used)
                    heapq.heappush(free,top[1])
                if free:
                    room = heapq.heappop(free)
                    heapq.heappush(used,(meet[1],room))
                    rooms[room] += 1
                    mx = max(mx,rooms[room])
                else:
                    # print(meet,used,free)
                    top = heapq.heappop(used)
                    heapq.heappush(used,(top[0]+diff,top[1]))
                    rooms[top[1]] += 1
                    mx = max(mx,rooms[top[1]])
        return rooms.index(mx)
                    
                    
                

            