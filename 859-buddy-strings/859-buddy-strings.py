class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        a = Counter(s)
        b = Counter(goal)
        count = 0
        max_ = 0
        for i in range(len(s)):
            max_ = max(max_, a[s[i]],a[goal[i]])
            if a[s[i]] != b[s[i]] or a[goal[i]] != b[goal[i]]:
                return False
            if s[i] != goal[i]:
                count += 1
        return count == 2 or ((s == goal )and max_ > 1)
                
        