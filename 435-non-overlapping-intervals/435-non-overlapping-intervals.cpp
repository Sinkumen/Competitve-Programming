class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size()==0) return 0;
        
        sort(intervals.begin(),intervals.end());
        int prevEnd = intervals[0][1];
        int count=0;
        
        for(int i=1;i<intervals.size();i++){
            int& curStart =intervals[i][0];
            int& curEnd =intervals[i][1];
            if(curStart<prevEnd){
                //overlap
                count++;
                //remove the one with larger end
                //update prevEnd
                prevEnd = std::min(curEnd,prevEnd);
            }else{
                //no overlapping
                //update end to the new end
                prevEnd = curEnd;
            }    
        }
        
        return count;
    }
};