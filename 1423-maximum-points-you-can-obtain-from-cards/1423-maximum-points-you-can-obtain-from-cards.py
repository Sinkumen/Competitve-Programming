class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = n - k
        summ = sum(cardPoints[:window])
        ans = summ
        left = 0
        right = window
        while right < n:
            summ -= cardPoints[left]
            summ += cardPoints[right]
            ans = min(summ,ans)
            left += 1
            right += 1
        return sum(cardPoints) - ans
            
            
            
            