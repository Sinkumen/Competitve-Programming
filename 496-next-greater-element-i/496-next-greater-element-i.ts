var nextGreaterElement = function(nums1, nums2) {
    let stack = [];
    let result = [];
    let map = new Map();
    
    stack.push(nums2[0]);
    
    for(let i = 1; i < nums2.length; i++){
        let current = nums2[i];
        
        while(stack.length > 0 && current > stack[stack.length - 1]){
            let top = stack.pop();
            map.set(top, current);
        }
        
        stack.push(current);
    }
    
    while(!(stack.length === 0)){
        let top = stack.pop();
        map.set(top, -1);
    }
   
    for(let i = 0; i < nums1.length; i++){
       let resVal = map.get(nums1[i]);
       result.push(resVal);
    }
    
    return result;
    
};