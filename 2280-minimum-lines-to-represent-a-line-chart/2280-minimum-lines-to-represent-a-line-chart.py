from fractions import Fraction
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()

        prev = None
        ans = 0
        for i in range(1,len(stockPrices)):
            day,price =  stockPrices[i]
            pday,pprice = stockPrices[i-1]
            slope = Fraction((price-pprice), (day-pday))
            if slope != prev:
                ans += 1
                prev = slope
        return ans