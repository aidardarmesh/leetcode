from typing import *

class Solution:
    '''
    Main strategy in BS template 2 is to half search space
    until search space is sloped to zero and return left pointer
    in the end
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l+r) // 2
            
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        
        return l
