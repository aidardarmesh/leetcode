from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right = [0]*N, [0]*N
        left_max = right_max = 0
        ans = 0
        
        for i in range(N):
            left_max = max(left_max, height[i])
            left[i] = left_max
        
        for i in range(N-1, -1, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max
        
        for i in range(N):
            ans += min(left[i], right[i]) - height[i]
        
        return ans
