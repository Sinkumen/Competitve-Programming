class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for char in s:
            ans = max(ans,len(stack))
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
        return ans