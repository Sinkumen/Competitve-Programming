class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")

        for cmd in dirs:
            if cmd and cmd != "." and cmd != "..":
                stack.append(cmd)
            elif stack and cmd == "..":
                stack.pop()

        return "/"+"/".join(stack)
