from typing import *

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = -1
        max_val = float('-inf')
        
        for i, val in enumerate(nums):
            if val > max_val:
                max_index = i
                max_val = val
        
        for i, val in enumerate(nums):
            if i != max_index and val * 2 > max_val:
                return -1
        
        return max_index
