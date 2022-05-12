class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        def dfs(res,v):
            if len(res) == len(nums):
                ans.add(tuple(res))
                return
            for j in range(len(nums)):
                if j not in v:
                    v.add(j)
                    res.append(nums[j])
                    dfs(res,v)
                    res.pop()
                    v.remove(j)
        dfs([],set())
        return ans
            
            