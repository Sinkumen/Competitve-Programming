var sortColors = function (nums) {
  const red = [];
  const white = [];
  const blue = [];

  for (let index = 0; index < nums.length; index++) {
    const element = nums[index];
    if (element === 0) {
      red.push(element);
    }
    if (element === 1) {
      white.push(element);
    }
    if (element === 2) {
      blue.push(element);
    }
  }
  nums.splice(0, nums.length);
  let srtd = [...red, ...white, ...blue];
  nums.push(...srtd);
};
sortColors([2, 0, 2, 1, 1, 0]);
