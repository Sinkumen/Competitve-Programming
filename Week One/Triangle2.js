var drawTriangleTwo = (n) => {
  for (i = 1; i <= n; i++) {
    // let space = '';
    let stars = "";
    for (j = n - i; j >= 1; j--) {
      stars += " ";
    }
    for (k = 0; k < 2 * i - 1; k++) {
      stars += "*";
    }
    console.log(stars);
  }
};

drawTriangleTwo(5);
