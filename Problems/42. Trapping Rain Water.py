from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0]*n, [0]*n
        max_left = max_right = 0
        res = 0
        
        for i in range(n):
            max_left = max(max_left, height[i])
            left[i] = max_left
        
        for i in range(n-1, -1, -1):
            max_right = max(max_right, height[i])
            right[i] = max_right
        
        for i in range(n):
            res += min(left[i], right[i]) - height[i]
        
        return res
