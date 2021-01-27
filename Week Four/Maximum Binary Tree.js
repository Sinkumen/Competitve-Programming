var constructMaximumBinaryTree = function (nums) {
  let max = nums[0];

  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    max = num > max ? num : max;
  }
  let index = nums.indexOf(max);
  let left = nums.slice(0, index);
  let right = nums.slice(index + 1);

  if (left.length && right.length) {
    return new TreeNode(
      max,
      constructMaximumBinaryTree(left),
      constructMaximumBinaryTree(right)
    );
  }
  if (left.length && !right.length) {
    return new TreeNode(max, constructMaximumBinaryTree(left), null);
  }
  if (!left.length && right.length) {
    return new TreeNode(max, null, constructMaximumBinaryTree(right));
  }
  if (!left.length && !right.length) {
    return new TreeNode(max, null, null);
  }
};
