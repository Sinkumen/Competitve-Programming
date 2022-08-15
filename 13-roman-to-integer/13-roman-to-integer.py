class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c == "V" and i > 0 and s[i-1] == "I":
                ans += (nums[c] - nums[s[i-1]]) - nums[s[i-1]]
            elif c == "X" and i > 0 and s[i-1] == "I":
                ans += (nums[c] - nums[s[i-1]]) - nums[s[i-1]]
            elif c == "L" and i > 0 and s[i-1] == "X":
                ans += (nums[c] - nums[s[i-1]]) - nums[s[i-1]]
            elif c == "C" and i > 0 and s[i-1] == "X":
                ans += (nums[c] - nums[s[i-1]]) - nums[s[i-1]]
            elif c == "D" and i > 0 and s[i-1] == "C":
                ans += (nums[c] - nums[s[i-1]]) - nums[s[i-1]]
            elif c == "M" and i > 0 and s[i-1] == "C":
                ans += (nums[c] - nums[s[i-1]]) - nums[s[i-1]]
            else:
                ans += nums[c]
        return ans
            