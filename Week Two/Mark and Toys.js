const maximumToys = (array, k) => {
  let totalPrice = 0;
  let count = 0;
  const prices = [];
  while (totalPrice <= k) {
    let min = array[0];
    let minIndex = 0;
    for (let i = 0; i < array.length; i++) {
      if (array[i] < min) {
        min = array[i];
        minIndex = i;
      }
    }
    if (totalPrice + min <= k) {
      totalPrice += min;
      count++;
      array.splice(minIndex, 1);
      prices.push(min);
    } else {
      break;
    }
  }
  console.log({ prices, count, totalPrice });
};

maximumToys([1, 12, 5, 111, 200, 1000, 10], 50);
