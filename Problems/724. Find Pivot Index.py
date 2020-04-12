from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        prefix = [0] * n
        
        def get_at(arr, idx):
            if idx < 0 or idx >= len(arr):
                return 0
            
            return arr[idx]
        
        for i in range(n):
            prefix[i] = get_at(prefix, i-1) + nums[i]
        
        for i in range(n):
            if get_at(prefix, i-1) == get_at(prefix, n-1) - get_at(prefix, i):
                return i
        
        return -1
