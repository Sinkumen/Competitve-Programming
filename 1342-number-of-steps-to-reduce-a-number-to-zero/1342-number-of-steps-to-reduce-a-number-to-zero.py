class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(bin(num)[2:])-1 + bin(num).count("1")