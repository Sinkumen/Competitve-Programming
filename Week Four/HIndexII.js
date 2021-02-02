var hIndex = function (citations) {
  let len = citations.length;
  if (len === 0) {
    return 0;
  }
  if (len === 1) {
    if (citations[0] === 0) {
      return 0;
    } else {
      return 1;
    }
  }

  let start = 0;
  let end = len - 1;

  while (start <= end) {
    let mid = start + Math.floor((end - start) / 2);
    let middle = citations[mid];
    if (middle >= len - mid) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return len - start;
};
