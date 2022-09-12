class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens)-1
        score = 0
        while left <= right:
            if power < tokens[left]:
                if score >= 1:
                    if left != right:
                        score -= 1
                        power += tokens[right]
                        print(score,power)
                    right -= 1
                else:
                    return score
            else:
                score += 1
                power -= tokens[left]
                left += 1
        return score