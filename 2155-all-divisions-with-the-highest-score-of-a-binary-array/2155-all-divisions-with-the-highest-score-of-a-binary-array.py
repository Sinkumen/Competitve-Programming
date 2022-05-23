class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        pre = [0]
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            pre.append(zeros)
        suff = [0]*len(nums)
        ones = 0
        mapping = defaultdict(list)
        maxx = pre[-1]
        mapping[pre[-1]].append(len(pre)-1)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 1:
                ones += 1
            suff[i] = ones
            maxx  = max(maxx,ones+pre[i])
            mapping[ones+pre[i]].append(i)
        
        return mapping[maxx]
            
            
            