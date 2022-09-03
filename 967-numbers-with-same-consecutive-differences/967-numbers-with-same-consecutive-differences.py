class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        def dfs(dig):
            nonlocal ans
            if len(dig) == n:
                ans.add(int("".join(dig)))
                return
            
            last = int(dig[-1])
            nxts = set([last + k,last - k])
            for nxt in nxts:
                if 0 <= nxt < 10:
                    dig.append(str(nxt))
                    dfs(dig)
                    dig.pop()
                
        for i in range(1,10):
            dfs([str(i)])
        return ans
                