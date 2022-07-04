class Solution:
    def candy(self, ratings: List[int]) -> int:

        pre = [1]
        count = 1
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                count += 1
            else:
                count = 1
            pre.append(count)
        count = 1
        ans = max(pre[-1],1)
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                count += 1
            else:
                count = 1
            ans += max(pre[j],count)
            
        return ans
                