function eraseOverlapIntervals(intervals) {
  // sort by end time
  intervals.sort(([, aEnd], [, bEnd]) => aEnd - bEnd);
  let count = 0;
  for(let i = 1 ; i < intervals.length ; i++){
    const [startA, endA] = intervals[i - 1];
    const [startB, endB] = intervals[i];
    
    // if there's an overlap
    // then remove the interval with the greater
    // end time, and we know for sure that
    // interval at index i has greater end time
    // when compared to interval at index i - 1,
    // because we sorted the array by end time
    if(endA > startB){
      intervals[i] = [startA, endA];
      count++;
    }
  }
  return count;
};