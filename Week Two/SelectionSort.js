const SelectionSort = (array) => {
  for (let i = 0; i < array.length; i++) {
    let min = array[i];
    let minIndex = i;

    for (let j = i + 1; j < array.length; j++) {
      const current = array[j];
      if (current < min) {
        min = current;
        minIndex = j;
      }
    }
    swap(i, minIndex, array);
  }
  console.log(array);
};

const swap = (indexA, indexB, array) => {
  const temp = array[indexA];
  array[indexA] = array[indexB];
  array[indexB] = temp;
};

SelectionSort([5, 3, 2, 1, 4, 0, 12]);
