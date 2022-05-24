class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_ = 0
        for i in range(len(s)): 
            if s[i] == ")":
                if stack[-1] == -1 or s[stack[-1]] != "(" :
                    stack.append(i)
                else:
                    stack.pop()
                max_ = max(max_,i-stack[-1])
            else:
                stack.append(i)
        return max_
                