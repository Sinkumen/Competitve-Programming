class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        paths = []
        for d in dirs:
            if d and d != "." and d != "..":
                paths.append(d)
            elif paths and d and d == "..":
                paths.pop()
        return "/" + "/".join(paths)
        