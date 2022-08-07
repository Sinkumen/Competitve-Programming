class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        curTiime = 0
        history = {}
        days = 0
        for task in tasks:
            if task in history:
                diff = curTiime - history[task]-1
                if diff < space:
                    curTiime += (space - diff)
                history[task] = curTiime
            else:
                history[task] = curTiime
            curTiime += 1
            
                
        return curTiime
        