var findBottomLeftValue = function (root) {
  if (!root) {
    return null;
  }
  let dist = 0;
  return helper(root, dist).node.val;
};

var helper = (root, dist) => {
  if (!root) {
    return null;
  }
  if (!root.left && !root.right) {
    return { node: root, length: dist };
  }
  if (root.left && !root.right) {
    let left = helper(root.left, dist + 1);
    return left;
  }
  if (!root.left && root.right) {
    let right = helper(root.right, dist + 1);
    return right;
  }
  let left = helper(root.left, dist + 1);
  let right = helper(root.right, dist + 1);

  console.log(left, right);
  return left.length >= right.length ? left : right;
};
