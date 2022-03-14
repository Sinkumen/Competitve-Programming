class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {"}":"{",")":"(","]":"["}
        for c in s:
            if c in closing:
                if stack and stack[-1] == closing[c]: stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack