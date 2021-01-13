var pancakeSort = function (arr) {
  const sorted = arr.sort((a, b) => a - b);
  if (sorted.join("") === arr.join("")) {
    return [];
  }
  const flipIndexes = [];
  let { max, maxIndex } = findMax(arr);
};

const findMax = (arr) => {
  let max = arr[0];
  let maxIndex = 0;
  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    max = element > max ? element : max;
    maxIndex = element > max ? i : maxIndex;
  }
  return { max, maxIndex };
};

console.log([1, 2, 3].join("") === [1, 3, 2].join(""));
