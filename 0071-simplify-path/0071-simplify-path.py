class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []
        for s in dirs:
            if s and s not in {".",".."}:
                stack.append(s)
            if stack and s == "..":
                stack.pop()
        return "/"+"/".join(stack)
                