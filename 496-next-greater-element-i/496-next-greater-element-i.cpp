class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n=nums2.size();
        unordered_map<int,int>m;
        for(int i=0;i<n;i++){
            m[nums2[i]]=i;
        }
        stack<int>st;
        vector<int>result(n,-1);
        for(int i=0;i<n;i++){
            while(!st.empty() && nums2[st.top()]<nums2[i]){
                result[st.top()]=nums2[i];
                st.pop();
            }
            st.push(i);
        }
        vector<int>ans(nums1.size(),-1);
        for(int i=0;i<nums1.size();i++){
            ans[i]=result[m[nums1[i]]];
        }
        return ans;
    }
};