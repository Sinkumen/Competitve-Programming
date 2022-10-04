class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int n=heights.size();
        int maxArea=0;
        for(int i=0;i<=n;i++){
            while(!st.empty() && (i==n || heights[i]<=heights[st.top()])){
                int height=heights[st.top()];
                st.pop();
                int width;
                if(st.empty()) 
                    width=i;
                else
                    width=(i-1)-(st.top()+1)+1;
                maxArea=max(maxArea,height*width);
            }
            st.push(i);
        }
        return maxArea;
    }
};