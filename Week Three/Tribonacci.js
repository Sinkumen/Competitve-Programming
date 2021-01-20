function tribonacci(n) {
  var trib = [0, 1, 1];
  if (n < 3) return trib.slice(0, n);
  for (var i = 3; i <= n; i++) {
    trib.push(trib[i - 1] + trib[i - 2] + trib[i - 3]);
  }
  return trib.pop();
}
console.log(tribonacci(36));
