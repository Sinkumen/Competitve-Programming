class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(rem,closed,res):
            if not rem:
                ans.append("".join(res) + ")"*(n-closed))
                return
            res.append("(")
            dfs(rem-1,closed,res)
            res.pop()
            if n-rem > closed:
                res.append(")")
                dfs(rem,closed + 1,res)
                res.pop()
           
        dfs(n,0,[])
        return ans
                
                