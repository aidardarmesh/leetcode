from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        
        for i in range(len(heights)):
            left = right = i
            
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            
            while right < len(heights) and heights[right] >= heights[i]:
                right += 1
            
            max_rect = max(max_rect, (right-left-1) * heights[i])
        
        return max_rect
