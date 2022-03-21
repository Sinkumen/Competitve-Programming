class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_inds = {}
        n = len(s)
        
        for i in range(n):
            last_inds[s[i]] = i
        
        start,end = -1,last_inds[s[0]]
        
        ans = []
        #print(last_inds)
        for i in range(n):
         #   print(start,end,i)
            end = max(end,last_inds[s[i]])
            if end == i:
                ans.append(end - start)
                start = end
        
        return ans
            