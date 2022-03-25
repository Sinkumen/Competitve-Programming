class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        a = []
        for i in range(len(costs)):
            cost = costs[i]
            a.append((cost[1]-cost[0],i))
        a.sort(key = lambda x :abs(x[0]))
        at = 0
        bt = 0
        ans = 0
        for i in range(len(a)-1,-1,-1):
            if a[i][0] > 0:
                if at < n:
                    ans += min(costs[a[i][1]])
                    at += 1
                else:
                    ans += max(costs[a[i][1]])
                    bt += 1
            else:
                if bt < n:
                    ans += min(costs[a[i][1]])
                    bt += 1
                else:
                    ans += max(costs[a[i][1]])
                    at += 1
        return ans
        
                