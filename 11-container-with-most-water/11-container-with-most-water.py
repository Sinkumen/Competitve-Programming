class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height)-1
        while i<j:
            area = min(height[i],height[j]) * (j-i)
            maxArea = area if area > maxArea else maxArea
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
           

        return maxArea
                
        