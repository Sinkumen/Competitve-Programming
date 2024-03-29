class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        srtd = sorted(count.values(),reverse=True)
        ans = 0
        prev = float("inf")
        for i in range(len(srtd)):
            if prev <= srtd[i]:
                diff = (srtd[i]-prev) + 1
                srtd[i] -= diff
                ans += diff
            if srtd[i]:
                prev = srtd[i]
        return ans