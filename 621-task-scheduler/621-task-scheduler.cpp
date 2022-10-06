class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if(n==0)
            return tasks.size();
        
        int m=0;
        unordered_map<char,int> map;
        for(int i=0;i<tasks.size();i++){
            map[tasks[i]]++;
            m=max(m,map[tasks[i]]);
        }
        
        int count_max=0;
        for(auto it:map){
            if(it.second==m)
                count_max++;
        }
        
        int x = (n+1)*(m-1)+(count_max);
        int s = tasks.size();
        return max(s,x);
    }
};