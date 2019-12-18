from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        def get_at(arr, index):
            if index < 0 or index >= len(arr):
                return 0
            
            return arr[index]
        
        N = len(nums)
        prefix = []
        
        for i in range(N):
            prefix.append(get_at(prefix, i-1) + nums[i])
        
        for i in range(N):
            if get_at(prefix, i-1) == get_at(prefix, N-1) - get_at(prefix, i):
                return i
        
        return -1
