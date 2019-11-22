from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Strategy is to remain one element at the end
        If mid element is more than rightmost one, get rid off left part
        Else, from right part
        '''
        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l+r) // 2
            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        return nums[l]
