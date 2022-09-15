class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(rem,closed,res):
            if not rem:
                res.append(")"*(n-closed))
                ans.append("".join(res))
                res.pop()
                return
            if n-rem > closed:
                res.append(")")
                dfs(rem,closed + 1,res)
                res.pop()
                
                res.append("(")
                dfs(rem-1,closed,res)
                res.pop()
            else:
                res.append("(")
                dfs(rem-1,closed,res)
                res.pop()
        dfs(n,0,[])
        return ans
                
                