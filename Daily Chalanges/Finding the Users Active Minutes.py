class Solution:
    def findingUsersActiveMinutes(self, logs, k: int):
        UAM = {}

        for log in logs:
            if log[0] in UAM:
                UAM[log[0]].add(log[1])
            else:
                UAM[log[0]] = set([log[1]])
        res = [0]*k
        for value in UAM.values():
            n = len(value)-1
            res[n] += 1
        return res
