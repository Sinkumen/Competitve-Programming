class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        idx = 0
        for i in range(len(s)):
            
            while idx and s[i] != part[idx]:
                idx -= 1
            if s[i] == part[idx]:
                stack.append((s[i],idx))
                idx += 1 
            else:
                if stack and stack[-1][0] == part[idx]:
                    stack.append((s[i],1))
                    idx += 2
                else:
                    stack.append((s[i],-1))
            if idx >= len(part):
                while idx:
                    stack.pop()
                    idx -= 1
                if stack:
                    idx = stack[-1][1] + 1

        return "".join([x[0] for x in stack])
                
                