var searchBST = function (root, val) {
  if (!root) {
    return null;
  }

  if (root.val === val) {
    return root;
  }

  if (root.val > val) {
    return searchBST(root.left, val);
  } else {
    return searchBST(root.right, val);
  }
};

var searchBSTIteratively = function (root, val) {
  if (!root) {
    return null;
  }

  let current = root;
  while (current) {
    if (current.val === val) {
      return current;
    }
    if (current.val > val) {
      current = current.left;
    } else {
      current = current.right;
    }
  }
  return null;
};
