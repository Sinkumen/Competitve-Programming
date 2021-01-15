var superDigit = (n, k = 1) => {
  var num = n.toString().repeat(k);
  let currentSum = 0;
  for (let i = 0; i < num.length; i++) {
    const dig = Number.parseInt(num[i]);

    currentSum += dig;
  }
  if (currentSum < 10) {
    return currentSum;
  } else {
    return superDigit(currentSum);
  }
};
console.log(superDigit(148, 3));
