const ObjectCountingSort = (array) => {
  let maxPrice = array[0].price;
  for (let i = 0; i < array.length; i++) {
    const { price } = array[i];
    maxPrice = price > maxPrice ? price : maxPrice;
  }

  const temp = [];
  for (let i = 0; i < maxPrice + 1; i++) {
    temp.push([]);
  }

  for (let i = 0; i < array.length; i++) {
    temp[array[i].price].push(array[i]);
  }
  const sorted = [];

  for (let index = 0; index < temp.length; index++) {
    const element = temp[index];
    if (element.length) {
      for (let i = 0; i < element.length; i++) {
        const e = element[i];
        sorted.push(e);
      }
    }
  }
  console.log(sorted);
};

ObjectCountingSort([
  { name: "a", price: 2 },
  { name: "b", price: 5 },
  { name: "c", price: 4 },
  { name: "d", price: 1 },
  { name: "e", price: 3 },
]);
