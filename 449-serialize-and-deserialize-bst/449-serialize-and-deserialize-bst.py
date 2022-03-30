# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(node,res):
            if not node:
                return res
            res.append(str(node.val))
            preorder(node.left,res)
            preorder(node.right,res)
        res = []
        
        preorder(root,res)
        print(res)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def build(lst,lower,upper):
            if not lst or not lower <= lst[0] <= upper:
                return None
            
            cur = TreeNode(lst.pop(0))
            
            cur.left = build(lst,lower,cur.val)
            cur.right = build(lst,cur.val,upper)
            
            return cur
        preorder = [int(x) for x in data.split(",")] if data else []
        return build(preorder,float("-inf"),float("inf"))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans