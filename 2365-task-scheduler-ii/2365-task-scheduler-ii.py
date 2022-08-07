class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        curTime = 0
        history = {}
        days = 0
        for task in tasks:
            if task in history:
                diff = curTime - history[task]-1
                if diff < space:
                    curTime += (space - diff)
                history[task] = curTime
            else:
                history[task] = curTime
            curTime += 1
            
                
        return curTime
        