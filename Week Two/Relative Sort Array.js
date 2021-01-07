var relativeSortArray = function (arr1, arr2) {
  var duplicates = arr2.reduce(function (acc, el, i, arr) {
    if (arr.indexOf(el) !== i && acc.indexOf(el) < 0) acc.push(el);
    return acc;
  }, []);
  if (!duplicates.length) {
    const inBoth = [];
    const onlyInArr1 = [];
    for (let i = 0; i < arr1.length; i++) {
      const indexInArr2 = arr2.indexOf(arr1[i]);

      if (!(indexInArr2 < 0)) {
        inBoth.push(arr1[i]);
      } else {
        onlyInArr1.push(arr1[i]);
      }
    }
    inBoth.sort((a, b) => arr2.indexOf(a) - arr2.indexOf(b));
    onlyInArr1.sort((a, b) => a - b);
    console.log([...inBoth, ...onlyInArr1]);
    return [...inBoth, ...onlyInArr1];
  }
};

relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]);
