var sum2BigNumbers = (n1, n2) => {
  const num1 =
    n1.toString().length >= n2.toString().length
      ? n1.toString().split("").reverse()
      : n2.toString().split("").reverse();
  const num2 =
    n1.toString().length >= n2.toString().length
      ? n2.toString().split("").reverse()
      : n1.toString().split("").reverse();
  let sum = "";
  let carry = 0;
  for (let i = 0; i < num1.length; i++) {
    if (num2[i]) {
      let s = (
        Number.parseInt(num1[i]) +
        Number.parseInt(num2[i]) +
        carry
      ).toString();
      if (s.length === 1) {
        sum += s;
        carry = 0;
      } else {
        carry = Number.parseInt(s.split("")[0]);
        const n = s.split("")[1];
        sum += n;
      }
    } else {
      let s = (Number.parseInt(num1[i]) + carry).toString();
      if (s.length === 1) {
        sum += s;
        carry = 0;
      } else {
        carry = Number.parseInt(s.split("")[0]);
        const n = s.split("")[1];
        sum += n;
      }
    }
  }
  sum += carry ? carry.toString() : "";
  const finalSum = sum.split("").reverse().join("");
  console.log(finalSum);
  return finalSum;
};

sum2BigNumbers(99209, 803);
