class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []
        maxx = 0 
        for h in height:
            maxx = max(maxx,h)
            pre.append(maxx)
        maxx = 0 
        for i in range(len(height)-1,-1,-1):
            maxx = max(maxx,height[i])
            suf.append(maxx)
        suf.sort(reverse = True)
        ans = 0
        print(pre)
        print(suf)
        for i in range(len(height)):
            ans += min(pre[i],suf[i]) - height[i]
        return ans