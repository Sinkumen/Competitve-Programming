var search = function (nums, target) {
  let mid = ~~((nums.length - 1) / 2);
  let middle = nums[mid];

  if (middle === target) {
    return mid;
  }
  if (middle > target) {
    return search(nums.slice(0, mid), target);
  }
  if (middle < target) {
    let val = search(nums.slice(mid + 1), target);
    return val >= 0 ? mid + val + 1 : -1;
  }
  return -1;
};
