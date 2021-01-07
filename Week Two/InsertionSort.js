const InsertionSort = (array) => {
  for (let i = 1; i < array.length; i++) {
    const current = array[i];
    let index = i;
    for (let j = i - 1; j >= 0; j--) {
      if (current < array[j]) {
        swap(index, j, array);
        index--;
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

InsertionSort([4, 2, 5, 3, 1, 0]);
