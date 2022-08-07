class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        total = sum(candidates)
        
        def helper(i,summ,res):
            if summ == target:
                ans.add(tuple(res))
                return
            visited = set()
            for j in range(i,len(candidates)):
                n = candidates[j]
                if n not in visited:
                    visited.add(n)
                    if summ + n <= target:
                        res.append(n)
                        helper(j+1,summ+n,res)
                        res.pop()
                    else:
                        break
        if total >= target:
            helper(0,0,[])  
        return ans