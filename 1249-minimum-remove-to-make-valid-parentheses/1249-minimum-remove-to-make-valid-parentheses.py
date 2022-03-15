class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lst = list(s)
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == ")": 
                if not stack:
                    lst[i] = ""
                else:
                    stack.pop()
            elif c == "(":
                stack.append((c,i))
        for par in stack:
            lst[par[1]] = ""
            
        return "".join(lst)
            