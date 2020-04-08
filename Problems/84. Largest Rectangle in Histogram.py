from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area, stack = 0, [-1]
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()]*(i-stack[-1]-1))
            
            stack.append(i)
        
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        
        return max_area
