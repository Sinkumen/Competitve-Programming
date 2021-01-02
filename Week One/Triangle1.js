var drawTriangleOne = (n) => {
  for (i = 1; i <= n; i++) {
    let stars = "";
    for (j = 1; j <= i; j++) {
      stars += "*";
    }
    console.log(stars);
  }
};

drawTriangleOne(4);
