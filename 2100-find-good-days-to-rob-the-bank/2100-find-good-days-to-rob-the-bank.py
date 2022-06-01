class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        if time == 0:
            return [x for x in range(len(security))]
        
        pre = [0]
        count = 0
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                count += 1
            else:
                count = 0
            pre.append(count)
            
        suf = [0]*len(security)
        count = 0
        ans = []
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                count += 1
            else:
                count = 0
            if pre[i] >= time and count >= time:
                ans.append(i)
        return ans
                
            