class Solution:
    def minPartitions(self, n: str) -> int:
        max_ = 0
        for x in n:
            max_ = max(max_,int(x))
        return max_
        