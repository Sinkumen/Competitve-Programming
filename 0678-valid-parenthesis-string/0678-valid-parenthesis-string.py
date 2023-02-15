class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append((char,i))
            elif char == "*":
                star.append((char,i))
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack:
            top,i = stack.pop()
            if star and star[-1][1] > i:
                star.pop()
            else:
                return False
            
        
        return True
                    
        