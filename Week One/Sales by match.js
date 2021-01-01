function sockMerchant(n, ar) {
  if (n >= 1 && n <= 100) {
    let pair = 0;
    for (let i = 0; i < n; i++) {
      const color = ar[i];
      if (color >= 1 && color <= 100) {
        let count = 0;
        for (let j = i + 1; j < n; j++) {
          if (color === ar[j]) {
            count++;
          }
        }
        pair += count % 2;
      } else {
        console.log("invalid color");
        return 0;
      }
    }
    console.log(pair);
    return pair;
  } else {
    console.log("out of range");
    return 0;
  }
}

sockMerchant(7, [1, 2, 1, 2, 1, 30, 2]);
