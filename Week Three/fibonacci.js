const fibonacci = (n) => {
  let a = 0;
  let b = 1;
  for (let i = 0; i < n; i++) {
    const temp = a;
    a = b;
    b = temp + b;
  }
  return b;
};

console.log(fibonacci(5));
