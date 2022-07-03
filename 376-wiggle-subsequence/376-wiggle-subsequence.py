class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dfs(i,isPos):
            res = 0
            for j in range(i+1,len(nums)):
                if isPos and nums[j] < nums[i]:
                    res = max(res,dfs(j,not isPos))

                if isPos == False and nums[j] > nums[i]:
                    res = max(res,dfs(j,not isPos))
                    
                if isPos == None and nums[j] != nums[i]:
                    cur = (nums[j] - nums[i]) > 0
                    res = max(res,dfs(j,cur))
            return res + 1
        
        return dfs(0,None)
                
            
        
                
                
                
                