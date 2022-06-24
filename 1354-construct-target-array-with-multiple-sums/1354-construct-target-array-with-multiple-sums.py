class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        heap = [-num for num in target]
        heapq.heapify(heap)
        total = sum(target)
        while heap:
            top = -heapq.heappop(heap)
            if top == 1:
                return True
            rest = total - top
            if top  <= rest or not rest:
                return False
            mod = top % rest
            if mod:
                heapq.heappush(heap,-mod)
            else:
                heapq.heappush(heap,-rest)
            total = rest + mod
            
        