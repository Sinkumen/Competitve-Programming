var largestPerimeter = function (A) {
  const sorted = A.sort((a, b) => a - b).reverse();
  for (let i = 0; i < sorted.length; i++) {
    const base = sorted[i];
    const sideA = sorted[i + 1];
    const sideB = sorted[i + 2];
    if (sideA + sideB > base) {
      return sideB + sideA + base;
    }
  }
  return 0;
};

console.log(largestPerimeter([2, 1, 2]));
console.log(largestPerimeter([3, 6, 2, 3]));
console.log(largestPerimeter([1, 2, 1]));
