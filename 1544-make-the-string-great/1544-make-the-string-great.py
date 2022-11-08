class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char.isupper() and stack[-1] ==  char.lower():
                stack.pop()
            elif char.islower() and stack[-1] ==  char.upper():
                stack.pop()
            else: stack.append(char)
        return "".join(stack)