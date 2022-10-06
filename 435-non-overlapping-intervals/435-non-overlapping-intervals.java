class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->a[1]-b[1]);

        int freeAt = Integer.MIN_VALUE;
        int count = 0;

        for(int i =0;i<intervals.length;i++){
            if(freeAt <= intervals[i][0]){
                freeAt = intervals[i][1];
                count++;
            }
        }

        return intervals.length - count;
    }
}