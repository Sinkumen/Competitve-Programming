class Solution {
    public PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
    public PriorityQueue<Integer> right = new PriorityQueue<>();
    
    public double[] medianSlidingWindow(int[] nums, int k) {
        for(int i=0; i<k; i++) {
            addNum(nums[i]);
        }
        
        double[] ans = new double[nums.length - k + 1];
        int j = 0;
        ans[j] = findMedian();
        for(int i=k; i<nums.length; i++) {
            remove(nums[j]);
            addNum(nums[i]);
            j += 1;
            ans[j] = findMedian();
        }
        
        return ans;
    }

    public void addNum(int num) {
        if(right.peek() == null) {
            left.add(num);
        } else if(num > right.peek()){
            right.add(num);
        } else {
            left.add(num);
        }
        
        if(Math.abs(left.size() - right.size()) > 1) {
            if(left.size() > right.size()) {
                right.add(left.remove());
            } else {
                left.add(right.remove());
            }
        }
    }
    
    public void remove(int num) {
        if(right.size() > 0 && num >= right.peek()) {
            right.remove(num);
        } else {
            left.remove(num);
        }
        
        if(Math.abs(left.size() - right.size()) > 1) {
            if(left.size() > right.size()) {
                right.add(left.remove());
            } else {
                left.add(right.remove());
            }
        }
    }
    
    public double findMedian() {
        if(left.size() > right.size()) {
            return (double)left.peek();
        } else if(right.size() > left.size()) {
            return (double)right.peek();
        } else {
            return (left.peek() / 2.0) + (right.peek() / 2.0);
        }
    }
}