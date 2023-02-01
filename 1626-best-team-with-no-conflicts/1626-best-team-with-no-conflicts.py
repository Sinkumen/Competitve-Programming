class Solution:
     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        # Initialize dynamic programming array and score_age variable
        dp = [0]*(1 + max(ages))
        player_score = sorted(zip(scores, ages))

        # Iterate through sorted pairs of score and age to find maximum attainable score
        for score, age in player_score:
            dp[age] = score + max(dp[:age + 1])

        return max(dp)