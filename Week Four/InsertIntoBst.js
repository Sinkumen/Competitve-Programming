var insertIntoBST = function (root, val) {
  let newNode = new TreeNode(val);
  if (!root) {
    return newNode;
  }

  let current = root;
  while (current.right || current.left) {
    if (current.val > val) {
      if (current.left) {
        current = current.left;
      } else {
        current.left = newNode;
        return root;
      }
    } else {
      if (current.right) {
        current = current.right;
      } else {
        current.right = newNode;
        return root;
      }
    }
  }
  if (current.val > val) {
    current.left = newNode;
  } else {
    current.right = newNode;
  }
  return root;
};
