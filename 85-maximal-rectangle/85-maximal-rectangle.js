function maximalRectangle(matrix) {
  const streaks = [];
  let max = 0;

  for (let i = 0; i < matrix.length; i++) {
    streaks[i] = [];

    for (let j = 0; j < matrix[i].length; j++) {
      streaks[i][j] =
        matrix[i][j] === "0" ? 0 : 1 + (i === 0 ? 0 : streaks[i - 1][j]);
    }
  }

  for (let i = 0; i < matrix.length; i++) {
    const stack = [];

    for (let j = 0; j <= matrix[i].length; j++) {
      while (
        stack.length > 0 &&
        (j === matrix[i].length || streaks[i][j] <= streaks[i][stack[stack.length-1]])
      ) {
        const height = streaks[i][stack.pop()];
        const width = stack.length === 0 ? j : j - stack[stack.length-1] - 1;

        max = Math.max(max, width * height);
      }

      stack.push(j);
    }
  }

  return max;
}