var countNegatives = function (grid) {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] < 0) {
        count++;
      }
    }
  }
  return count;
};

var countNegativesONM = function (grid) {
  if (grid[0][0] < 0) {
    return grid.length * grid[0].length;
  }
  let count = 0;
  let all = [];
  for (let i = 0; i < grid.length; i++) {
    all.push(...grid[i]);
  }
  for (let j = 0; j < all.length; j++) {
    if (all[j] < 0) {
      count++;
    }
  }
  return count;
};
