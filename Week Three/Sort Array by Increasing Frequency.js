/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function (nums) {
  let frequencies = {};

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    if (typeof frequencies[n] !== "undefined") {
      frequencies[n] = frequencies[n] + 1;
    } else {
      frequencies[n] = 1;
    }
  }
  let freqArray = [];

  for (let key in frequencies) {
    freqArray.push({ val: key, frequency: frequencies[key] });
  }
  let sorted = [];
  freqArray.sort((a, b) => b.val - a.val);
  freqArray.sort((a, b) => a.frequency - b.frequency);
  for (let i = 0; i < freqArray.length; i++) {
    const elem = freqArray[i];
    for (let j = 0; j < elem.frequency; j++) {
      sorted.push(elem.val);
    }
  }
  return sorted;
};

console.log(frequencySort([2, 3, 1, 3, 2]));
