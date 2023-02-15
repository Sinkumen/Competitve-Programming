class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        mp = {}
        for a,b in pairs:
            mp[a] = b
            mp[b] = a
        pref = defaultdict(dict)
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                val = preferences[i][j]
                pref[i][val] = j
        def check(a,b):
            for pr in preferences[a]:
                if pr == b:
                    break
                if pref[pr][a] < pref[pr][mp[pr]]:
                    return False
                
            return True
        ans = 0
        for f,s in pairs:
            if not check(f,s):
                ans += 1
            if not check(s,f):
                ans += 1
        return ans
                            