var hIndex = function (citations) {
  if (!citations.length) {
    return 0;
  }
  if (citations.length === 1) {
    if (citations[0] === 0) {
      return 0;
    }
    return 1;
  }
  let sorted = citations.sort((a, b) => a - b);
  let hindex = 0;
  for (let i = 0; i < sorted.length; i++) {
    let res = sorted.slice(i);
    if (sorted[i] >= sorted.length - i) {
      return sorted.length - i;
    }
  }
  return hindex;
};
