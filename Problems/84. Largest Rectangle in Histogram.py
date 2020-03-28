from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                left = stack.pop()
                max_area = max(max_area, heights[left] * (i - stack[-1] - 1))
            
            stack.append(i)
        
        while stack[-1] != -1:
            left = stack.pop()
            max_area = max(max_area, heights[left] * (len(heights) - stack[-1] - 1))
        
        return max_area
