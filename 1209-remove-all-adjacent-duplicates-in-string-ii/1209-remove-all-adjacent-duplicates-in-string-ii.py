class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack:
                top = stack[-1]
                if s[i] == top[0]:
                    if top[1] == k-1:
                        for i in range(k-1):
                            stack.pop()
                    else:
                        stack.append((s[i],top[1]+1))
                else:
                    stack.append((s[i],1))
            else:
                stack.append((s[i],1))
        ans = ""
        for char,count in stack:
            ans += char
        return ans
        