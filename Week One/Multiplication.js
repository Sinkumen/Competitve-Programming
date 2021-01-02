var multiplication = (n1, n2) => {
  const positive = (n1 < 0 && n2 > 0) || (n1 > 0 && n2 < 0) ? false : true;
  const nm1 = n1 > 0 ? n1 : n1 * -1;
  const nm2 = n2 > 0 ? n2 : n2 * -1;
  const num1 =
    nm1.toString().length >= nm2.toString().length
      ? nm1.toString().split("").reverse()
      : nm2.toString().split("").reverse();
  const num2 =
    nm1.toString().length >= nm2.toString().length
      ? nm2.toString().split("").reverse()
      : nm1.toString().split("").reverse();
  const toBeSummed = [];

  for (let i = 0; i < num2.length; i++) {
    const multiplyer = num2[i];
    let multiple = "";
    let carry = 0;
    for (let j = 0; j < num1.length; j++) {
      const toBeMultiblied = num1[j];
      let s = (
        Number.parseInt(toBeMultiblied) * Number.parseInt(multiplyer) +
        carry
      ).toString();
      if (s.length === 1) {
        multiple += s;
        carry = 0;
      } else {
        carry = Number.parseInt(s.split("")[0]);
        const n = s.split("")[1];
        multiple += n;
      }
    }
    multiple += carry ? carry.toString() : "";
    const finalSum = multiple.split("").reverse().join("");
    toBeSummed.push(finalSum);
  }
  console.log(toBeSummed);
  let prev = 0;
  for (let i = 0; i < toBeSummed.length; i++) {
    let zeros = "";
    for (let j = 0; j < i; j++) {
      zeros += "0";
    }
    const multi = toBeSummed[i] + zeros;
    prev = sum2BigNumbers(multi, prev);
  }
  console.log("answer: ", positive ? prev : "-" + prev);
};

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
  return finalSum;
};

multiplication(4579, 78579);
