class Solution {
    public int largestRectangleArea(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(right, n);
        
        Stack<Integer> mono_stack = new Stack<>();
        for(int i = 0 ; i < n; i++) {
            while(!mono_stack.isEmpty() && nums[mono_stack.peek()] > nums[i]) {
                right[mono_stack.peek()] = i;
                mono_stack.pop();
            }
            left[i] = mono_stack.isEmpty() ? -1 : mono_stack.peek();
            mono_stack.push(i);
        }
        
        int ans = 0;
        for(int i = 0 ; i < n ; i++) {
            ans = Math.max(ans, (right[i] - left[i] - 1) * nums[i]); 
        }
      return ans;                     
    }
}