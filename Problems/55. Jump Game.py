from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        from collections import deque
        
        deq = deque([0])
        
        while deq:
            idx = deq.popleft()
            
            if idx == n-1:
                return True
            
            for delta in range(1, nums[idx]+1):
                deq.append(idx + delta)
        
        return False
