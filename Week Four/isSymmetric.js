var isSameTree = function (p, q) {
  if (!p && !q) {
    return true;
  }
  if (!p || !q) {
    return false;
  }

  if (p.val != q.val) {
    return false;
  }

  return isSameTree(p.left, q.right) && isSameTree(p.right, q.left);
};
var isSymmetric = function (root) {
  return isSameTree(root, root);
};
