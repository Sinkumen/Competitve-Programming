const findMedian = (array) => {
  if (array.length % 2) {
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
    console.log(sorted[(array.length - 1) / 2]);
    return sorted[(array.length - 1) / 2];
  }
  return 0;
};

findMedian([0, 1, 2, 4, 6, 5, 3]);
