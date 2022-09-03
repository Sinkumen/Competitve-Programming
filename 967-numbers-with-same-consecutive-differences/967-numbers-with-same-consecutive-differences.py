class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        def dfs(dig):
            nonlocal ans
            if len(dig) == n:
                ans.add(int("".join(dig)))
                return
            last = int(dig[-1])
            if 0 <= last + k < 10:
                dig.append(str(last + k))
                dfs(dig)
                dig.pop()
            if 0 <= last - k < 10:
                dig.append(str(last - k))
                dfs(dig)
                dig.pop()
                
        for i in range(1,10):
            dfs([str(i)])
        return ans
                