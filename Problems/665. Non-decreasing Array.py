from typing import *

import sys

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
            
        return p is None or p == 0 or p == len(nums) - 2 \
                or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]

s = Solution()

assert s.checkPossibility([4,2,3]) == True
assert s.checkPossibility([4,2,1]) == False
assert s.checkPossibility([3,4,2,3]) == False
assert s.checkPossibility([-1,4,2,3]) == True