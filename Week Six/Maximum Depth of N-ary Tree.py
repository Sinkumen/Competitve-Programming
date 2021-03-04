class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        if len(root.children) == 0:
            return 1
        maxx = 0
        for child in root.children:
            depth = self.maxDepth(child)
            maxx = depth if depth > maxx else maxx
        return maxx + 1
