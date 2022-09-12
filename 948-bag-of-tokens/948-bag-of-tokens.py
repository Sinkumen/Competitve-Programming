class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens)-1
        score = 0
        while left <= right:
            if power < tokens[left] and score >= 1 and left != right:
                score -= 1
                power += tokens[right]
                right -= 1
                
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
            left += 1
        return score