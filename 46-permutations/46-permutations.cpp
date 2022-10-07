class Solution {
public:
    
    // Backtracking
    void permutation(vector<int> &nums,vector<vector<int>> &result, int i,int n){
        if(i==n){
            result.push_back(nums);
            return ;
        }

        for(int j=i;j<=n;j++){
            swap( nums[i],nums[j]);
            permutation(nums,result,i+1,n);
            swap( nums[i],nums[j]);
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        
        permutation(nums,result,0,nums.size()-1);
        
        return result;
    }

};