from fractions import Fraction
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        prev = None
        ans = 1 if len(stockPrices) > 1 else 0
        for i in range(2,len(stockPrices)):
            day,price =  stockPrices[i]
            pday,pprice = stockPrices[i-1]
            ppday,ppprice = stockPrices[i-2]
            slope = (price-pprice) * (pday-ppday)
            slope2 = (pprice-ppprice) * (day-pday)
            if slope != slope2:
                ans += 1
                
        return ans