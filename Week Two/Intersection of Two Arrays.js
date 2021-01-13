const intersection = function (nums1, nums2) {
  const intersection = [];
  for (let i = 0; i < nums1.length; i++) {
    const elementOne = nums1[i];
    for (let j = 0; j < nums2.length; j++) {
      const elementTwo = nums2[j];
      if (elementOne === elementTwo && !intersection.includes(elementOne)) {
        intersection.push(elementOne);
      }
    }
  }
  console.log(intersection);
  return intersection;
};

intersection([8, 0, 3], [0, 0]);
