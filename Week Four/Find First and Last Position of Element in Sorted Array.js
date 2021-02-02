var searchRange = function (nums, target) {
  let index = search(nums, target);
  console.log(index);
  if (index >= 0) {
    let left = search(nums.slice(0, index), target);
    let right = search(nums.slice(index), target);
    let rindex = index;
    console.log(left, right);
    while (right >= 0) {
      right = search(nums.slice(rindex + 1), target);
      rindex++;
    }
    //  searchRange([1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8], 8);
    let lindex = index;
    while (left >= 0) {
      left = search(nums.slice(0, lindex - 1), target);
      lindex--;
    }
    return [lindex, rindex - 1];
  }
  return [-1, -1];
};

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

console.log(
  searchRange([1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8], 4)
);
