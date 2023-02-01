class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        srtd = sorted(range(len(growTime)),key = lambda x: -growTime[x])
        print(srtd)
        ans = 0
        prev = 0
        for i in srtd:
            ans += plantTime[i]
            prev = max(prev - plantTime[i],growTime[i])
        ans += prev
        return ans