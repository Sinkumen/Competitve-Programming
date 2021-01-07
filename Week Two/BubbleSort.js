const BubbleSort = (array) => {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      const first = array[j];
      const next = array[j + 1];
      if (first > next) {
        swap(j, j + 1, array);
      }
    }
  }
  console.log(array);
};

const swap = (indexA, indexB, array) => {
  const temp = array[indexA];
  array[indexA] = array[indexB];
  array[indexB] = temp;
};

BubbleSort([2, 6, 4, 3, 0, 100, 58, 5, 1]);
