const countingSort = (array) => {
  const temp = [];
  let max = array[0];
  for (let i = 0; i < array.length; i++) {
    const element = array[i];
    max = element > max ? element : max;
  }

  for (let i = 0; i < max + 1; i++) {
    temp.push(0);
  }
  for (let i = 0; i < array.length; i++) {
    const element = array[i];
    temp[element] = temp[element] + 1;
  }
  const sorted = [];
  for (let index = 0; index < temp.length; index++) {
    const element = temp[index];
    if (element) {
      for (let j = 0; j < element; j++) {
        sorted.push(index);
      }
    }
  }
  return sorted;
};

console.log(countingSort([2, 1, 5, 8]));
