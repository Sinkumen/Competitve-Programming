var solution = function (isBadVersion) {
  return function (n) {
    let start = 0;
    let end = n;
    let bad = -1;
    while (start <= end) {
      let mid = ~~((start + end) / 2);
      if (isBadVersion(mid)) {
        end = mid - 1;
        bad = mid;
      } else {
        start = mid + 1;
      }
    }

    return bad;
  };
};
