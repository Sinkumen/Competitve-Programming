class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        vals = 0
        ans = 0
        for val in sorted(count.values(),reverse=True):
            vals += val
            ans += 1
            if vals >= len(arr)//2:
                break
        return ans