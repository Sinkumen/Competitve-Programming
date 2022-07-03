class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        width = horizontalCuts[0]
        for i in range(1,len(horizontalCuts)):
            diff = horizontalCuts[i] - horizontalCuts[i-1]  
            width = max(width,diff)
            
        height = verticalCuts[0] 
        for j in range(1,len(verticalCuts)):
            diff = verticalCuts[j] - verticalCuts[j-1]  
            height = max(height,diff)
            
        return height * width % mod