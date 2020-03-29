from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area, stack = 0, [-1]

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                H = heights[stack.pop()]
                R = i
                L = stack[-1]
                max_area = max(max_area, H * (R - L - 1))
            
            stack.append(i)
        
        while stack[-1] != -1:
            H = heights[stack.pop()]
            R = len(heights)
            L = stack[-1]
            max_area = max(max_area, H * (R - L - 1))
        
        return max_area
