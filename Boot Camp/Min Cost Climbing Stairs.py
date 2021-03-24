class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        memory = {}

        def findMin(i):
            nonlocal memory
            if i == len(cost)-1 or i == len(cost)-2:
                memory[i] = cost[i]
                return cost[i]

            one = findMin(i+1) if i+1 not in memory else memory[i+1]
            two = findMin(i+2) if i+2 not in memory else memory[i+2]
            memory[i] = min(one, two) + cost[i]
            return min(one, two) + cost[i]

        return min(findMin(0), findMin(1))
