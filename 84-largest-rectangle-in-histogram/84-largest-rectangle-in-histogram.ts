function largestRectangleArea(heights) {
    const stack = [];
    
    let area = 0;
    let max = 0;
    
    heights.push(0);
    
    for (const height of heights) {
        
        let multiplier = 0;
        
        while (stack.length > 0 && height < stack[stack.length - 1][0]) {
            const tallest = stack.pop();
            multiplier += 1 + tallest[1];
            const area = multiplier * tallest[0];
            
            if (area > max) {
                max = area;
            }
        }
        
        stack.push([height, multiplier]);
        
    }
    
    return max;
}