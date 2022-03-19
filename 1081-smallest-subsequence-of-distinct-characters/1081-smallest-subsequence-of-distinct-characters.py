class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = [-1]*26
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if last[ord(c)-ord("a")] == -1:
                last[ord(c)-ord("a")] = i
                
        visited = set()
        
        stack = []
        
        
        for i in range(len(s)):
            c = s[i]
            
            if c in visited:
                continue
            while stack and stack[-1][0] >= c:
                top = stack[-1]
                idx = ord(top) - ord("a")
                if i < last[idx]:
                    stack.pop()
                    visited.remove(top)
                else:
                    break
            stack.append(c)
            visited.add(c)
        return "".join(stack)