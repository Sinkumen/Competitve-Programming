class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0
        for val in count.values():
            if val  == 1:
                return -1
            ans += ceil(val/3)
        return ans