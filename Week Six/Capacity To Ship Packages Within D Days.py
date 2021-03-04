class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        start = min(weights)
        end = sum(weights)

        while start <= end:
            middle = start + (end - start)//2
            if self.checkDays(weights, middle) > D:
                start = middle + 1
            else:
                end = middle - 1
        return end + 1

    def checkDays(self, weights, weight):
        totalWeight = 0
        days = 0
        for itr in weights:
            totalWeight += itr
            if itr > weight:
                return float("inf")
            if totalWeight > weight:
                totalWeight = itr
                days += 1
        return days + 1
