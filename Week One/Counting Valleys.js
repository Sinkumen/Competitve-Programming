function countingValleys(steps, path) {
  if (steps >= 2 && steps <= Math.pow(10, 6)) {
    const pathes = path.split("");
    let vally = 0;
    let step = 0;
    for (let i = 0; i < steps; i++) {
      const element = pathes[i];
      if (element === "U" || "D") {
        if (element === "U") {
          step++;
        }
        if (element === "D") {
          if (step === 0) {
            vally++;
          }
          step--;
        }
      } else {
        return 0;
      }
    }
    console.log(vally);
    return vally;
  } else {
    return 0;
  }
}

countingValleys(10, "UDUUUDUDDD");
