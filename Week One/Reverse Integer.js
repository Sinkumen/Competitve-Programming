var reverse = function (x) {
  const strNum = x.toString();
  let array = strNum.split("");
  let newStr = array.reverse().join("");
  const reversed = Number.parseInt(x < 0 ? "-" + newStr : newStr);
  if (Math.pow(-2, 31) >= reversed || reversed >= Math.pow(2, 31) - 1) {
    console.log(0);
    return 0;
  } else {
    console.log(reversed);
    return reversed;
  }
};

reverse(123);
