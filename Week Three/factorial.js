const factorial = (n) => {
  if (n <= 0 || n === 1) {
    return n;
  } else {
    return n * factorial(n - 1);
  }
};

console.log(factorial(1));
