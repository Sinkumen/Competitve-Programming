'''
1 2 3 4 5

2 3 4 5 5
3 4 5 6 5
4 5 6 6 6
5 6 7 7 6
6 7 8 7 7
7 8 8 8 8
8 9 9 9 8
9 10 9 10 9
10 10 10 11 10
11 11 11 11 11
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ = min(nums)
        return sum([x-min_ for x in nums])