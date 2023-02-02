class Solution:
    def numberOfWays(self, s: str) -> int:
        dic = defaultdict(int)
        ans = 0
        for i in range(len(s)):
            if s[i] == "0":

                ans += dic["01"]
                dic["0"] += 1
                dic["10"] += dic["1"]
            else:
                ans += dic["10"]
                dic["1"] += 1
                dic["01"] += dic["0"]
        return ans
                