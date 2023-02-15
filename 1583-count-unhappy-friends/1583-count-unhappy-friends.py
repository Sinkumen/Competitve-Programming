class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        mp = {}
        for a,b in pairs:
            mp[a] = b
            mp[b] = a
        def check(a,b):
            for pr in preferences[a]:
                if pr == b:
                    break
                for temp in preferences[pr]:
                    if temp == a:
                        return False
                    if temp == mp[pr]:
                        break
            return True
        ans = 0
        for f,s in pairs:
            if not check(f,s):
                ans += 1
            if not check(s,f):
                ans += 1
        return ans
                            