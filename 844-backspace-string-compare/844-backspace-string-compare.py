class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S):
            stack = []
            ptr = 0
            while ptr < len(S):
                if S[ptr] == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(S[ptr])
                ptr += 1
            return stack
        return build(s) == build(t)
            