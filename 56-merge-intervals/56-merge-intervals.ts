var merge = function(intervals) {
    intervals.sort((a,b)=> a[0] -b[0])
    let result = [intervals[0]];
    
    for(let i = 1; i < intervals.length; i++){
        let e1 = result[result.length - 1][1];
        let interval = intervals[i]
        if(e1 >= interval[0]){
            result[result.length - 1][1] = Math.max(e1, interval[1]);
        }else{
            result.push(interval)
        }
    }
   
    return result;
};