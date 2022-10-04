class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1) # Guarantee max area will be computed at last index
        max_area, stack = float('-inf'), []
        
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
            stack.append((index,h))
                
                
        return max_area