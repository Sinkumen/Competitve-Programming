class Solution:
    def sumNumbers(self, root) -> int:
        ans = 0

        def dfs(node, num):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(num+str(node.val))
                return
            if node.left:
                dfs(node.left, num+str(node.val))
            if node.right:
                dfs(node.right, num+str(node.val))
        if root:
            dfs(root, "")
        return ans
