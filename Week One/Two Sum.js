var twoSum = function (nums, target) {
  if (nums.length >= 2 && nums.length <= Math.pow(10, 3)) {
    if (target > Math.pow(-10, 9) && target < Math.pow(10, 9)) {
      for (let i = 0; i < nums.length; i++) {
        const first = nums[i];
        for (let j = i + 1; j < nums.length; j++) {
          const second = nums[j];
          if (
            first > Math.pow(-10, 9) &&
            first < Math.pow(10, 9) &&
            second > Math.pow(-10, 9) &&
            second < Math.pow(10, 9)
          ) {
            if (first + second === target) {
              console.log([i, j]);
              return [i, j];
            }
          } else {
            return 0;
          }
        }
      }
    } else {
      return 0;
    }
  } else {
    return 0;
  }
};

twoSum([2, 7, 11, 15], 9);
