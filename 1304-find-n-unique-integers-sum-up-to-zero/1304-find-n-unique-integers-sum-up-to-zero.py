class Solution:
    def sumZero(self, n: int) -> List[int]:
        s = 1
        total = 0 
        ans = []
        for i in range(n-1):
            s += i
            total += s
            ans.append(s)
        ans.append(-total)
        return ans
        
        