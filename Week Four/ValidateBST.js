var isValidBST = function (root) {
  return check(root.right, null, root.val) && check(root.left, root.val, null);
};

var check = (root, upper, lower) => {
  if (!root) {
    return true;
  }
  if (upper && upper < root.val) {
    return false;
  }
  if (lower && lower > root.val) {
    return false;
  }
  return check(root.right, null, root.val) && check(root.left, root.val, null);
};
