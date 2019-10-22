from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        
        return -1

s = Solution()

assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], 2) == -1