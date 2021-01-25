var rangeSumBST = function (root, low, high) {
  if (!root) {
    return 0;
  }
  let sum = 0;
  if (root.val <= high && root.val >= low) {
    sum = sum + root.val;
  }
  if (root.left) {
    sum = sum + rangeSumBST(root.left, low, high);
  }
  if (root.right) {
    sum = sum + rangeSumBST(root.right, low, high);
  }
  return sum;
};
