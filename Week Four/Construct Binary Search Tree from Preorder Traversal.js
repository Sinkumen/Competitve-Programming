var bstFromPreorder = function (preorder) {
  let root = null;
  for (let i = 0; i < preorder.length; i++) {
    root = insert(root, preorder[i]);
  }

  return root;
};
var insert = (root, val) => {
  if (!root) {
    return new TreeNode(val);
  }
  if (root.val > val) {
    root.left = insert(root.left, val);
  }
  if (root.val < val) {
    root.right = insert(root.right, val);
  }
  return root;
};
