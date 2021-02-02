var postorderTraversal = function (root) {
  let traversal = [];
  traverse(root, traversal);
  return traversal;
};

var traverse = (root, traversal) => {
  if (!root) {
    return traversal;
  }

  traverse(root.left, traversal);
  traverse(root.right, traversal);
  traversal.push(root.val);
};

var search = function (nums, target) {
  let middle = nums[nums.length / 2];
  let index = 0;
  if (middle > target) {
    search(nums.slice(0, ~~(nums.length / 2)));
  } else if (middle < target) {
    index += search(nums.slice(~~(nums.length / 2)));
  } else {
    return nums.length;
  }
  return index;
};
