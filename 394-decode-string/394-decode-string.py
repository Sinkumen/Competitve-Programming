class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            temp = []
            if s[i] == "]":
                while stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                multi = ""
                while stack and stack[-1].isdigit():
                    top = stack.pop()
                    multi = top + multi
                rep = "".join(temp[::-1])*int(multi)
                for c in rep:
                    stack.append(c)
            else:
                stack.append(s[i])
        return "".join(stack)
                
            
            
            