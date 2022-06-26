class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints)-k
        left,right = 0, window
        sum_ = sum(cardPoints[:window])
        min_ = sum_
        while right < len(cardPoints):
            sum_ = sum_ +  cardPoints[right] - cardPoints[left]
            min_ = min(min_,sum_)
            right += 1
            left += 1
        return sum(cardPoints) - min_