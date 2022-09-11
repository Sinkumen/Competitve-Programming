class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        srtd = sorted([(efficiency[i],i) for i in range(n)],reverse = True)
        ans,total = 0,0
        pre = []
        for i in range(n):
            while len(pre) >= k:
                total -= heapq.heappop(pre)
            total += speed[srtd[i][1]]
            heapq.heappush(pre,speed[srtd[i][1]])
            ans = max(ans,total*srtd[i][0])
        return ans % mod
            
        