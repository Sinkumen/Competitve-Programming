class Solution:
    def countOrders(self, n):
        ans = 1
        for i in range(1, n + 1):
            ans = ans * comb(2*i, 2) % (10**9 + 7)
        return ans